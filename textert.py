import boto3

def ocr_document(bucket_name, object_key):
    # Initialize the Textract client
    textract_client = boto3.client('textract')

    # Call Textract to detect text in the document
    response = textract_client.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': object_key
            }
        }
    )

    # Extract the detected text from the response
    detected_text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            detected_text += item['Text'] + '\n'

    return detected_text

# Example usage
bucket_name = 'sandy-0419044'
object_key = 'textert.jpeg'
detected_text = ocr_document(bucket_name, object_key)

# Print the detected text
print(detected_text)
