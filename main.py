import functions_framework
from google.cloud import storage
import base64
import json

@functions_framework.cloud_event
def enable_versioning_on_bucket(cloud_event):
    """
    Main Cloud Function to be triggered by Pub/Sub for 2nd Gen.
    Args:
        cloud_event (functions_framework.CloudEvent): The CloudEvent object.
    """
    # Decode the Pub/Sub message
    data = base64.b64decode(cloud_event.data['message']['data']).decode('utf-8')
    message_json = json.loads(data)

    # Extract the bucket name
    bucket_name = message_json.get('resource', {}).get('labels', {}).get('bucket_name')
    if not bucket_name:
        print("Bucket name not found in the message")
        return

    # Initialize the Cloud Storage client
    storage_client = storage.Client()

    try:
        # Get the bucket
        bucket = storage_client.get_bucket(bucket_name)

        # Enable versioning
        bucket.versioning_enabled = True
        bucket.patch()

        print(f"Versioning enabled for bucket: {bucket_name}")
    except Exception as e:
        print(f"Error enabling versioning for bucket {bucket_name}: {e}")

