import os
import json

import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')


def lambda_handler(event, context):
    user_message = event.get('message', 'Hello')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
    )
    reply = response['choices'][0]['message']['content']
    return {
        'statusCode': 200,
        'body': json.dumps({'reply': reply})
    }
