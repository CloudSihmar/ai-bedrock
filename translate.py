import boto3

def translate_document(input_bucket, input_key, output_bucket, output_key):
    # Initialize the Translate client
    translate_client = boto3.client('translate')

    # Retrieve the German document from S3
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=input_bucket, Key=input_key)
    german_text = response['Body'].read().decode('utf-8')

    # Translate the document from German to English
    translation = translate_client.translate_text(
        Text=german_text,
        SourceLanguageCode='de',
        TargetLanguageCode='en'
    )

    # Save the translated text to a file and upload it to S3
    translated_text = translation['TranslatedText']
    s3_client.put_object(Bucket=output_bucket, Key=output_key, Body=translated_text.encode('utf-8'))

    return translated_text

# Specify the S3 bucket and file keys for the input German document and output English document
input_bucket = 'sandy-0419044'
input_key = 'german.txt'
output_bucket = 'sandeep-stable-diffusion'
output_key = 'translated.txt'

# Translate the document and get the translated text
translated_text = translate_document(input_bucket, input_key, output_bucket, output_key)

# Print the translated text
print("Translated Text:")
print(translated_text)
