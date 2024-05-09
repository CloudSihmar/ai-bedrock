import boto3
import json
import os
import base64

# Define the prompt for the image
prompt_data = """
Provide me a 4k hd image of Buddha statue during the sunset
"""

# Define the prompt template
prompt_template = [{"text": prompt_data, "weight": 1}]

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

# Construct the payload for the model
payload = {
    "text_prompts": prompt_template,
    "cfg_scale": 10,
    "seed": 0,
    "steps": 50,
    "width": 1024,
    "height": 1024
}

body = json.dumps(payload)

# Specify the model ID
model_id = "stability.stable-diffusion-xl-v1"

# Invoke the model with the specified parameters
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Parse the response JSON
response_body = json.loads(response["body"].read().decode("utf-8"))

# Print the generated image
artifact = response_body.get("artifacts")[0]
image_encoded = artifact.get("base64").encode("utf-8")
image_bytes = base64.b64decode(image_encoded)

# Save the image to a file in the output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
file_name = f"{output_dir}/sandeep.png"
with open(file_name, "wb") as f:
    f.write(image_bytes)

# Upload the image to S3
s3_client = boto3.client('s3')
bucket_name = 'sandy-0419044'
s3_key = 'sandeep.png'
s3_client.upload_file(file_name, bucket_name, s3_key)
