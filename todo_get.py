import json
import boto3

def lambda_handler(event, context):
    dynamodb=boto3.resource("dynamodb","eu-west-1")
    table=dynamodb.Table("codu-todo")

    data=table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(data["Items"])
    }
