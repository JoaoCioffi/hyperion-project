from dotenv import load_dotenv
import boto3
import os

# boto3 is the AWS SDK library for Python.
dynamodb = boto3.resource("dynamodb",
                           region_name=os.getenv("AWS_REGION"),
                           endpoint_url=os.getenv("DYNAMO_ENDPOINT"),
                           aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
                           aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")) # Connect to local instance

table = dynamodb.Table('Books')

# The UpdateItem API allows you to update a particular item as identified by its key.
resp = table.update_item(
    Key={"Author": "John Grisham", "Title": "The Rainmaker"},
    # Expression attribute names specify placeholders for attribute names to use in your update expressions.
    ExpressionAttributeNames={
        "#formats": "Formats",
        "#audiobook": "Audiobook",
    },
    # Expression attribute values specify placeholders for attribute values to use in your update expressions.
    ExpressionAttributeValues={
        ":id": "8WE3KPTP",
    },
    # UpdateExpression declares the updates you want to perform on your item.
    # For more details about update expressions, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html
    UpdateExpression="SET #formats.#audiobook = :id",
)
