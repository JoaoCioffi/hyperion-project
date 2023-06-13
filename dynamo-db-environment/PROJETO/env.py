from dotenv import load_dotenv
import os

def environment(dotEnv=load_dotenv()):
    constants = {
        'database-endpoint':os.getenv('DYNAMO_ENDPOINT'),
        'aws-region':os.getenv('AWS_REGION'),
        'aws-secret-key-id':os.getenv('AWS_ACCESS_KEY_ID'),
        'aws-secret-access-key':os.getenv('AWS_SECRET_ACCESS_KEY')
    }
    return constants