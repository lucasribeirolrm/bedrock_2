import boto3
import json

client = boto3.client(service_name="bedrock-agent-runtime", region_name="us-east-1")

def handler(event, context):
    body = json.loads(event["body"])
    question = body.get("question")
    if question:
        response = client.retrieve_and_generate(
            input={"text": question},
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": "FSYOLHR9HA",
                    "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0",
                },
            },
        )
        answer = response.get("output").get("text")
        return {
            "statusCode": 200,
            "body": json.dumps({"answer": answer}),
        }
    return {
            "statusCode": 400,
            "body": json.dumps({"error": "Entre com uma pergunta!"}),
        }