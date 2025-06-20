# Terraform Deployment

This configuration provisions the AWS resources required for the English conversation API.

## Prerequisites
- Terraform v1.0 or later
- AWS credentials with permissions to create Lambda and API Gateway resources

## Usage
1. Package the Lambda function as described in the parent README and note the path to the resulting `function.zip` file.
2. Initialize and apply the Terraform configuration:
   ```bash
   cd terraform
   terraform init
   terraform apply -var="package_file=../function.zip" -var="openai_api_key=<your-key>"
   ```
3. After the apply completes, the API endpoint URL is printed as the `invoke_url` output.

You can then send POST requests with a JSON body like `{"message": "Hello"}` to receive a reply from ChatGPT 4o.
