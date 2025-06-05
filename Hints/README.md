# PROJECT VENUS HINTS
This directory contains some some hint files to help

Make sure:
    A bucket has been created in your project named PROJECTNAME-bucket
    Firestore database has been initialized
    Permissions to bucket for AllUsers - Legacy Bucket Reader
    Enable additional APIs as needed, and document them for future reference
    
Dockerfile - an example dockerfile for containering this app  
Sample Docker Build command  
Command: `docker build --tag venusapp .`  
Command: `docker images`

Sample Docker Run command (used for testing locally)
NOTE: Recent updates to Cloud Shell/Docker may not resolve $GOOGLE_CLOUD_PROJECT env variable sucessfully inside app - use --env  
Command: `docker run --rm --publish 8080:8080 --env GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT venusapp`
Command (from another terminal): `curl http://localhost:8080`  

Create Google Artifact Registry Repo  
Command: `gcloud artifacts repositories create venusapp --repository-format=docker --location=us-east1 --description="Venus App Docker Repository"`  

Sample Push to GCR  
Command: `gcloud auth configure-docker REGION-docker.pkg.dev`  
Command: `docker tag venusapp us-east1-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/venusapp/venusapp`  
Command: `docker push us-east1-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/venusapp/venusapp`  

Sample Cloud Build to do CI (continuous integration) using Cloud Build and Artifact Registry  
Command: `gcloud builds submit --region=us-east1 --config=cloudbuild.yaml`  