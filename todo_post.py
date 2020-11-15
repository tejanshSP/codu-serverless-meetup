import json
import boto3
import uuid

def lambda_handler(event, context):
    dynamodb=boto3.resource("dynamodb","eu-west-1")
    table=dynamodb.Table("codu-todo")
    table.put_item(
        ConditionExpression="attribute_not_exists(id)",
        Item={
            "id" : str(uuid.uuid4()),
            "task" : event["task"]
        }
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
