# PROJECT VENUS HINTS
This directory contains some some hint files to help

Make sure:
    A bucket has been created in your project named PROJECTNAME-bucket
    Firestore database has been initialized
    Permissions to bucket for AllUsers - Legacy Bucket Reader
    Enable APIs as you go, and document them for future reference
    
Dockerfile - an example dockerfile for containering this app  
Sample Docker Build command 
Command: `docker build --tag venusapp .`  
Command: `docker images`

Sample Docker Run command (used for testing locally)
NOTE: Recent updates to Cloud Shell/Docker may not resolve $GOOGLE_CLOUD_PROJECT env variable sucessfully inside app - use --env  
Command: `docker run --rm --publish 8080:8080 --env GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT venusapp`
Command (from another terminal): `curl http://localhost:8080`  

Create Google Artifact Registry Repo (replace REGION)  
Command: `gcloud artifacts repositories create venusapp --repository-format=docker --location=REGION--description="Venus App Docker Repository"`  

Sample Push to GCR (replace REGION and PROJECT_ID)  
Command: `gcloud auth configure-docker REGION-docker.pkg.dev`  
Command: `docker tag venusapp REGION-docker.pkg.dev/PROJECT_ID/venusapp/venusapp`  
Command: `docker push REGION-docker.pkg.dev/PROJECT_ID/venusapp/venusapp`  

Sample Cloud Build to do CI (continuous integration) using Cloud Build and Artifact Registry  
Command: `gcloud builds submit --region=us-east1 --config=cloudbuild.yaml`  