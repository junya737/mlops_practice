# English Conversation Service

This example shows how to build a simple English conversation API using AWS Lambda and the OpenAI API (ChatGPT).

## Deployment steps

1. Install the required Python package:
   ```bash
   pip install -r requirements.txt -t package/
   ```
2. Package the Lambda function:
   ```bash
   cd package && zip -r9 ../function.zip . && cd ..
   zip -g function.zip lambda_function.py
   ```
3. Create an AWS Lambda function (via the console or CLI) using Python 3.9 runtime and upload `function.zip`.
4. Set an environment variable `OPENAI_API_KEY` with your OpenAI API key.
5. Integrate the Lambda function with API Gateway to expose an HTTPS endpoint.

You can invoke the endpoint with a JSON payload:
```json
{"message": "How are you?"}
```
which returns a JSON response with ChatGPT's reply. When using API Gateway,
send this JSON as the request body so the Lambda function can parse it.
