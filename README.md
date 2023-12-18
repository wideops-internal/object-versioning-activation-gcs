# object-versioning-activation-gcs

How to install?

- First you will need to deploy this code to Cloud function 2nd Gen.
- Next, create Pub/Sub Topic and Pub/Sub subscriber with Push notifitcation to Cloud function URL
- Goto Cloud Log Router and create sink Destination to Pub/Sub (You've created from previous stage) with the following filter:
resource.type="gcs_bucket"
protoPayload.methodName="storage.buckets.create"
- Next, enable the Cloud Storage from IAM Access Audit with Write Events


That's it! 
