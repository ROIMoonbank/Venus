# ROI Training Inc - Venus Document Management System
# Last Edit: 2025-06-05

from google.cloud import firestore

def document_to_dict(doc):
    if not doc.exists:
        return None
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id
    return doc_dict

def next_page(limit=10, start_after=None):
    db = firestore.Client()

    query = db.collection(u'venusdoc').limit(limit).order_by(u'title')

    if start_after:
        # Construct a new query starting at this document.
        query = query.start_after({u'title': start_after})

    docs = query.stream()
    docs = list(map(document_to_dict, docs))

    last_title = None
    if limit == len(docs):
        # Get the last document from the results and set as the last title.
        last_title = docs[-1][u'title']
    return docs, last_title

def read(venusdoc_id):
    # [START venusapp_firestore_client]
    db = firestore.Client()
    venusdoc_ref = db.collection(u'venusdoc').document(venusdoc_id)
    snapshot = venusdoc_ref.get()
    # [END venusapp_firestore_client]
    return document_to_dict(snapshot)

def update(data, venusdoc_id=None):
    db = firestore.Client()
    venusdoc_ref = db.collection(u'venusdoc').document(venusdoc_id)
    venusdoc_ref.set(data)
    return document_to_dict(venusdoc_ref.get())

create = update

def delete(id):
    db = firestore.Client()
    venusdoc_ref = db.collection(u'venusdoc').document(id)
    venusdoc_ref.delete()