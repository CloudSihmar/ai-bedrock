import boto3

def convert_text_to_speech(bucket_name, input_key, output_key):
    # Initialize the Polly client
    polly_client = boto3.client('polly')

    # Read the text from the input file in the S3 bucket
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key=input_key)
    text = response['Body'].read().decode('utf-8')

    # Convert the text to speech
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',  # Output format of the speech audio
        VoiceId='Joanna'  # Voice to use for the speech
    )

    # Save the speech audio to the output file in the S3 bucket
    s3_client.put_object(Bucket=bucket_name, Key=output_key, Body=response['AudioStream'].read())

    print(f"Speech audio saved to s3://{bucket_name}/{output_key}")

# Specify the S3 bucket name and the input and output file keys
bucket_name = 'sandy-0419044'
input_key = 'reviews.txt'
output_key = 'voice-reviews.mp3'

# Convert the text file to speech and save it to the output file
convert_text_to_speech(bucket_name, input_key, output_key)
