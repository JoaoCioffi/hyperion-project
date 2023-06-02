from dotenv import load_dotenv
import boto3
import os

dotEnv=load_dotenv()

dynamodb = boto3.resource("dynamodb",
                           region_name=os.getenv("AWS_REGION"),
                           endpoint_url=os.getenv("DYNAMO_ENDPOINT"),
                           aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
                           aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")) # Connect to local instance

table = dynamodb.Table('Books')

resp = table.get_item(Key={"Author": "John Grisham", "Title": "The Rainmaker"})

print(resp['Item'])
