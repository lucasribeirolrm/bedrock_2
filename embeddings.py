import boto3
import json

client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

roupa = "calça jeans"

response = client.invoke_model(
    body=json.dumps(
        {
            "inputText": roupa,
        }
    ),
    modelId="amazon.titan-embed-text-v1",
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
print(response_body.get("embedding"))