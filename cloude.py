import boto3
import json

# Define the prompt for the poem
prompt_data = """
Act as a Shakespeare and write a poem on machine learning
"""

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

# Construct the payload for the model
payload = {
    "prompt": prompt_data,
    "maxTokens": 512,
    "temperature": 0.5,
    "topP": 0.8
}

# Convert the payload to JSON
body = json.dumps(payload)

# Specify the model ID
model_id = "ai21.j2-mid-v1"

# Invoke the model with the specified parameters
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Parse the response JSON
response_body = json.loads(response["body"].read().decode("utf-8"))

# Extract the generated text from the response
response_text = response_body["completions"][0]["data"]["text"]

# Print the generated text
print(response_text)
