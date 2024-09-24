import boto3
import json

client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

def generate_embedding(text):
    response = client.invoke_model(
        body=json.dumps({"inputText": text}),
        modelId="amazon.titan-embed-text-v1",
        accept="application/json",
        contentType="application/json",
    )
    response_body = json.loads(response.get("body").read())
    return response_body.get("embedding")