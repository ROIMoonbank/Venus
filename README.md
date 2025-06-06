# PROJECT VENUS
Vault Enabling Necessary User Storage (VENUS) is a document storage solution for storing important documents within Moonbank.  
Customers are provided with an interface allowing them to upload and view their documents.

## Clone in the Repo
Open Cloud Shell  
Clone in the `https://github.com/ROIMoonbank/Venus` repo  
    Command: `git clone https://github.com/ROIMoonbank/Venus`  
    Command: `cd Venus`

## VENUS Setup/Dependancies
Make sure you have a project set  
    Command: `gcloud config set project YOURPROJECTNAME`

Enable APIs that may be needed  
    Command: `gcloud services enable firestore.googleapis.com`  
    Command: `gcloud services enable firebaserules.googleapis.com`  
    Command: `gcloud services enable pubsub.googleapis.com`  
    Command: `gcloud services enable aiplatform.googleapis.com`  
    Command: `gcloud services enable clouderrorreporting.googleapis.com`  
    Command: `gcloud services enable cloudbuild.googleapis.com`  
    Command: `gcloud services enable artifactregistry.googleapis.com`  
    Command: `gcloud services list`  

Bucket named projectid-bucket  
    Command: `gcloud storage buckets create gs://$GOOGLE_CLOUD_PROJECT-bucket`  
    
BigQuery Dataset called "venus"  
    Command: `bq mk venus`

BigQuery Table called "resources" - starting schema  
    Command: `bq mk --schema messages:STRING -t venus.resources`

PubSub Topic called "activities"  
    Command: `gcloud pubsub topics create venus`

PubSub Subscription called "activites-catchall"  
    Command : `gcloud pubsub subscriptions create venus-catchall --topic=projects/$GOOGLE_CLOUD_PROJECT/topics/venus`

Firestore Default Database Creation/Initialization  
    Open Firestore  
    Click Create a Firestore Database  
    Database ID: (leave default)  
    Standard Edition  
    Configuration Options:  
        Firestore Native  
        Security Rules: Open  
    Location:  
        Multi-regional nam5  