# object-versioning-activation-gcs

How to install?

- Goto Cloud Log Router and create sink Destination to Pub/Sub (Can be created while creating the sink) with the following filter:
resource.type="gcs_bucket"
protoPayload.methodName="storage.buckets.create"
- Next, enable the Cloud Storage from IAM Access Audit with Write Events
- Then you will need to deploy this code to Cloud function 2nd Gen.

That's it! 
