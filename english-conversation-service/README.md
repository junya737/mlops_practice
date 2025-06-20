# English Conversation Service

This example shows how to build a simple English conversation API using AWS Lambda and the OpenAI API (ChatGPT).

The function defaults to the **gpt-4o** model. You can override this by setting the `OPENAI_MODEL` environment variable.

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
4. Set environment variables:
   - `OPENAI_API_KEY`: your OpenAI API key
   - `OPENAI_MODEL` (optional): model name (defaults to `gpt-4o`)
5. Integrate the Lambda function with API Gateway to expose an HTTPS endpoint, or provision the infrastructure with Terraform (see below).

You can invoke the endpoint with a JSON payload:
```json
{"message": "How are you?"}
```
which returns a JSON response with ChatGPT's reply.

## Terraform deployment

You can deploy the Lambda function and an API Gateway endpoint automatically using the files in the `terraform/` directory:

```bash
cd terraform
terraform init
terraform apply -var="package_file=../function.zip" -var="openai_api_key=<your-key>"
```

The output will contain an `invoke_url` value that you can use to call the service.
