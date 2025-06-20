import os
import json

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o")


def lambda_handler(event, context):
    user_message = event.get('message', 'Hello')
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": user_message}],
    )
    reply = response['choices'][0]['message']['content']
    return {
        'statusCode': 200,
        'body': json.dumps({'reply': reply})
    }
