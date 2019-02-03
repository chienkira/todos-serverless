import json
import logging
import os
import time
import uuid

from handlers.lib.api import handle_api_response
import boto3
dynamodb = boto3.resource('dynamodb')


@handle_api_response
def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['TODO_DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write item to the database
    table.put_item(Item=item)

    # create a response
    return item
