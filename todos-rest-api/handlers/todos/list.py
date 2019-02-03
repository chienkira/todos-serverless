import os

from handlers.lib.api import handle_api_response
import boto3
dynamodb = boto3.resource('dynamodb')


@handle_api_response
def list(event, context):
    table = dynamodb.Table(os.environ['TODO_DYNAMODB_TABLE'])

    # fetch all todos from the database
    result = table.scan()

    # create a response
    return result['Items']
