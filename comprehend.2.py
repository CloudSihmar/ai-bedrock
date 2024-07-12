import boto3
import pandas as pd
from io import BytesIO

def comprehend_sentiment(reviews):
    # Initialize the Comprehend client
    comprehend_client = boto3.client('comprehend')

    positive_count = 0
    negative_count = 0

    for review in reviews:
        # Call Comprehend to detect the dominant language in the review
        language_response = comprehend_client.detect_dominant_language(
            Text=review
        )
        dominant_language_code = language_response['Languages'][0]['LanguageCode']

        # Call Comprehend to analyze the sentiment of the review
        sentiment_response = comprehend_client.detect_sentiment(
            Text=review,
            LanguageCode=dominant_language_code
        )
        sentiment = sentiment_response['Sentiment']

        if sentiment == 'POSITIVE':
            positive_count += 1
        elif sentiment == 'NEGATIVE':
            negative_count += 1

    return positive_count, negative_count

def open_document(bucket_name, object_key):
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Get the document from S3
    response = s3_client.get_object(
        Bucket=bucket_name,
        Key=object_key
    )

    # Read the contents of the document
    excel_data = response['Body'].read()

    # Use pandas to read the Excel file
    df = pd.read_excel(BytesIO(excel_data))

    # Extract the review texts (assuming they are in a column named 'Review Text')
    reviews = df['Review Text'].tolist()

    return reviews

# Example usage
bucket_name = 'sandeep-07896'
object_key = 'reviews.xlsx'
try:
    reviews = open_document(bucket_name, object_key)
    positive_count, negative_count = comprehend_sentiment(reviews)
    print(f"Total Positive Reviews: {positive_count}")
    print(f"Total Negative Reviews: {negative_count}")
except Exception as e:
    print(f"Error: {e}")
