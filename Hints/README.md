# PROJECT VENUS HINTS
This directory contains some some hint files to help

Make sure:
    A bucket has been created in your project named PROJECTNAME-bucket
    Firestore database has been initialized
    Permissions to bucket for AllUsers - Legacy Bucket Reader
    

Dockerfile - an example dockerfile for containering this app  
Sample Docker Build command 
Command: `docker build --tag venusapp .`  
Command: `docker images`

Sample Docker Run command (used for testing locally  
NOTE: Recent updates to Cloud Shell/Docker may not resolve $GOOGLE_CLOUD_PROJECT env variable sucessfully inside app - use --env  
Command: `docker run --rm --publish 8080:8080 --env GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT venusapp`

Sample Push to GCR
Command: `docker build --tag venusapp .`  

Sample Cloud Build
Command: 'docker build