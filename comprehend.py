import boto3

def comprehend_document(bucket_name, object_key):
    # Initialize the Comprehend client
    comprehend_client = boto3.client('comprehend')

    # Call Comprehend to detect the dominant language in the document
    response = comprehend_client.detect_dominant_language(
        Text=open_document(bucket_name, object_key)
    )

    # Get the dominant language code
    dominant_language_code = response['Languages'][0]['LanguageCode']

    # Call Comprehend to analyze the sentiment of the document
    response = comprehend_client.detect_sentiment(
        Text=open_document(bucket_name, object_key),
        LanguageCode=dominant_language_code
    )

    # Get the overall sentiment
    sentiment = response['Sentiment']

    return sentiment

def open_document(bucket_name, object_key):
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Get the document from S3
    response = s3_client.get_object(
        Bucket=bucket_name,
        Key=object_key
    )

    # Read and return the contents of the document
    return response['Body'].read().decode('utf-8')

# Example usage
bucket_name = 'sandy-0419044'
object_key = 'reviews.txt'
try:
    sentiment = comprehend_document(bucket_name, object_key)
    print(sentiment)
except Exception as e:
    print(f"Error: {e}")
