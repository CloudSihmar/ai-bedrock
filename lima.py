import boto3
import json

prompt_data = """
Act as a poet and write a poem on artificial intellegenct
"""

#Initialize Bedrock Client
bedrock = boto3.client(service_name="bedrock-runtime")

#Construct a payload dictionary
payload = {
    "prompt": "[INST]" + prompt_data + "[/INST]",
    "max_gen_len": 512,
    "temperature": 0.5,
    "top_p": 0.9
}

#Convert Payload to JSON
body = json.dumps(payload)
model_id = "meta.llama2-70b-chat-v1"  

#invoke model
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

#Parse the response JSON
response_body = json.loads(response['body'].read().decode('utf-8'))
response_text = response_body['generation']
print(response_text)
