# ROI Training Inc - Venus Document Management System
# Last Edit: 6/18/2024
#
import os
from google.cloud import pubsub_v1

def sendpubsub(message):
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
    topic_id = "venus-messages"
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    data = message.encode("utf-8")
    future = publisher.publish(
        topic_path, data
    )
    return "Message Sent"

if __name__ == '__main__':
    sendpubsub("This is a test")