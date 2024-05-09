import json
import boto3

def detect_faces_in_image(bucket_name, file_name):
    # Create a Rekognition client
    rekognition_client = boto3.client('rekognition')

    # Detect faces in the image
    response = rekognition_client.detect_faces(
        Image={'S3Object':{'Bucket': bucket_name, 'Name': file_name}},
        Attributes=['ALL']  # Optional: specify which face attributes to detect
    )

    # Print the detected faces
    for face_detail in response['FaceDetails']:
        print(json.dumps(face_detail, indent=2))

# Specify the S3 bucket name and file name
bucket_name = 'Bucketname'
file_name = 'imagename'

# Call the function to detect faces in the image
detect_faces_in_image(bucket_name, file_name)
