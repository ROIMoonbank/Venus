# ROI Training Inc - Venus Document Management System
# Last Edit: 2025-05-22

import logging
import firestore
from flask import current_app, flash, Flask, redirect, render_template
from markupsafe import Markup
from google.cloud import error_reporting
from flask import request, url_for

import google.cloud.logging
import storage
import messages
import thumbnail
import ai

def upload_image_file(img):
    """
    Upload the user-uploaded file to Google Cloud Storage and retrieve its
    publicly-accessible URL.
    """
    if not img:
        return None

    public_url = storage.upload_file(
        img.read(),
        img.filename,
        img.content_type
    )

    current_app.logger.info(
        'Uploaded file %s as %s.', img.filename, public_url)

    return public_url

app = Flask(__name__)
app.config.update(
    SECRET_KEY='secret',
    MAX_CONTENT_LENGTH=8 * 1024 * 1024,
    ALLOWED_EXTENSIONS=set(['png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'])
)

app.debug = False
app.testing = False

if not app.testing:
    logging.basicConfig(level=logging.INFO)
    client = google.cloud.logging.Client()
    # Attaches a Google Stackdriver logging handler to the root logger
    client.setup_logging()


@app.route('/')
def list():
    start_after = request.args.get('start_after', None)
    venusdocs, last_title = firestore.next_page(start_after=start_after)

    return render_template('list.html', venusdocs=venusdocs, last_title=last_title)


@app.route('/venusdocs/<venusdoc_id>')
def view(venusdoc_id):
    venusdoc = firestore.read(venusdoc_id)
    return render_template('view.html', venusdoc=venusdoc)


@app.route('/venusdocs/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        # If an image was uploaded, update the data to point to the new image.
        image_url = upload_image_file(request.files.get('image'))

        if image_url:
            data['imageUrl'] = image_url

        venusdoc = firestore.create(data)

        return redirect(url_for('.view', venusdoc_id=venusdoc['id']))

    return render_template('form.html', action='Add', venusdoc={})


@app.route('/venusdocs/<venusdoc_id>/edit', methods=['GET', 'POST'])
def edit(venusdoc_id):
    venusdoc = firestore.read(venusdoc_id)

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        # If an image was uploaded, update the data to point to the new image.
        image_url = upload_image_file(request.files.get('image'))

        if image_url:
            data['imageUrl'] = image_url

        venusdoc = firestore.update(data, venusdoc_id)

        return redirect(url_for('.view', venusdoc_id=venusdoc['id']))

    return render_template('form.html', action='Edit', venusdoc=venusdoc)


@app.route('/venusdocs/<venusdoc_id>/delete')
def delete(venusdoc_id):
    firestore.delete(venusdoc_id)
    return redirect(url_for('.list'))


@app.route('/logs')
def logs():
    logging.info('Hey, you triggered a custom log entry. Good job!')
    flash(Markup('''You triggered a custom log entry. You can view it in the
        <a href="https://console.cloud.google.com/logs">Cloud Console</a>'''))
    return redirect(url_for('.list'))


@app.route('/pubsub')
def pubsubmessage():
    messages.sendpubsub("Pub Sub Test" )
    logging.info('PubSub Message Sent!')
    flash(Markup('''You have sent a PubSub message. You can view it in the
        <a href="https://console.cloud.google.com/cloudpubsub">Cloud Console</a>'''))
    return redirect(url_for('.list'))

@app.route('/errors')
def errors():
    raise Exception('This is an intentional exception.')


# Add an error handler that reports exceptions to Operations  Error
# Reporting. Note that this error handler is only used when debug
# is False
@app.errorhandler(500)
def server_error(e):
    client = error_reporting.Client()
    client.report_exception(
        http_context=error_reporting.build_flask_context(request))
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
