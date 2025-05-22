# ROI Training Inc - Venus Document Management System
# Last Edit: 2025-05-22

import logging
import google.cloud.logging
import vertexai
from vertexai.generative_models import GenerativeModel, Part

def analyzeimage(imagepath):
    gcspath = imagepath.replace("https://storage.googleapis.com/","gs://")
    vertexai.init(location="us-central1")
    model = GenerativeModel(model_name="gemini-2.0-flash-001")
    response = model.generate_content(
        [
            Part.from_uri(
                gcspath,
                mime_type="image/jpeg",
            ),
            "What is shown in this image?",
        ]
    )
    logging.info('Image was processed by Vertex AI: ' + response.text)
    return(response.text)