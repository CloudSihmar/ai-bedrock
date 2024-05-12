import boto3

# Initialize the Amazon Transcribe client
transcribe_client = boto3.client('transcribe')

# Specify the S3 bucket name and the path to the audio file
bucket_name = 'Bucket-name'
file_key = 'file-name'

# Specify the language code for the audio
language_code = 'en-US'  # For example, 'en-US' for US English

# Specify the job name for the transcription job
job_name = 'your_job_name'

# Start the transcription job
response = transcribe_client.start_transcription_job(
    TranscriptionJobName=job_name,
    LanguageCode=language_code,
    MediaFormat='mp3',  # Change this to match your audio file format
    Media={
        'MediaFileUri': f's3://{bucket_name}/{file_key}'
    },
    OutputBucketName=bucket_name,  # Optional: Specify an output bucket for the transcription results
    OutputKey=f'{job_name}.json',  # Optional: Specify the output file name
    Settings={
        'ShowSpeakerLabels': False,  # Disable speaker labeling
    }
)

print(f"Transcription job started with JobName: {job_name}")
