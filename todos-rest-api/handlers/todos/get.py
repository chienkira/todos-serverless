import os

from handlers.lib.api import handle_api_response
import boto3
dynamodb = boto3.resource('dynamodb')


@handle_api_response
def get(event, context):
    table = dynamodb.Table(os.environ['TODO_DYNAMODB_TABLE'])

    # fetch item from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    return result['Item']
