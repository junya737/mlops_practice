variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project" {
  description = "Prefix for resource names"
  type        = string
  default     = "english-conversation"
}

variable "package_file" {
  description = "Path to the Lambda deployment package"
  type        = string
}

variable "openai_api_key" {
  description = "OpenAI API key"
  type        = string
  sensitive   = true
}

variable "openai_model" {
  description = "OpenAI model name"
  type        = string
  default     = "gpt-4o"
}
