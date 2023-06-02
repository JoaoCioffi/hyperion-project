from dotenv import load_dotenv
import boto3
import os
from boto3.dynamodb.conditions import Key

dotEnv=load_dotenv()

# boto3 is the AWS SDK library for Python.
dynamodb = boto3.resource("dynamodb",
                           region_name=os.getenv("AWS_REGION"),
                           endpoint_url=os.getenv("DYNAMO_ENDPOINT"),
                           aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
                           aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")) # Connect to local instance

table = dynamodb.Table('Books')

# When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
# We're using the Key object from the Boto3 library to specify that we want the attribute name ("Author")
# to equal "John Grisham" by using the ".eq()" method.
resp = table.query(KeyConditionExpression=Key('Author').eq('John Grisham'))

print("The query returned the following items:")
for item in resp['Items']:
    print(item)
