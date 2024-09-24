import json
from rag import handler

question = input("Digite sua pergunta:")

event = {
    "body": json.dumps({"question": question})
}

response = handler(event, {})

response_body = json.loads(response["body"])
print(response_body["answer"])