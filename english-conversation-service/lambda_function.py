import os
import json

import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')


def lambda_handler(event, context):
    """Handle Lambda invocation for a simple English chat API."""
    payload = event
    if isinstance(event, dict) and 'body' in event:
        try:
            payload = json.loads(event['body'] or '{}')
        except json.JSONDecodeError as e:
            logging.error(f"JSONDecodeError: {e}. Invalid JSON: {event['body']}")
            payload = {}

    user_message = payload.get('message', 'Hello')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
    )
    reply = response['choices'][0]['message']['content']
    return {
        'statusCode': 200,
        'body': json.dumps({'reply': reply})
    }

