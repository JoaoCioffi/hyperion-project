from boto3.dynamodb.conditions import Key,Attr
from botocore.exceptions import ClientError
from data_source import loadData
import env
import boto3
import json
import asyncio
import pandas as pd
import decimal

env=env.environment()
tables=loadData.tablesGenerator()
dynamodb=boto3.resource(
                            "dynamodb",
                            region_name=env['aws-region'],
                            endpoint_url=env['endpoint-url'],
                            aws_access_key_id=env['aws-access-key-id'], 
                            aws_secret_access_key=env['aws-secret-access-key']
                        ) # Connect to local instance

class TB_REGISTRO():
    
    def __init__(self):
        super(TB_REGISTRO.self).__init__()
    
    @classmethod
    async def createTable(self,table_name='TB_REGISTRO'):
        
        # table attributes
        attribute_definitions=[
            {
                'AttributeName': 'NUM_BO',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'ANO_BO',
                'AttributeType': 'N'
            }
        ]

        # table primary keys
        key_schema=[
            {
                'AttributeName': 'NUM_BO',
                'KeyType': 'HASH'  # partition key
            },
            {
                'AttributeName': 'ANO_BO',
                'KeyType': 'RANGE'  # classification key
            }
        ]

        # capacity settings
        provisioned_throughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
        
        try:
            table=dynamodb.create_table(
                TableName=table_name,
                AttributeDefinitions=attribute_definitions,
                KeySchema=key_schema,
                ProvisionedThroughput=provisioned_throughput
            )
            table.wait_until_exists()
        
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceInUseException':
                print('Table already exists, skipping...')
            else:
                return e

    @classmethod
    async def insertItems(
                            self,
                            table_name='TB_REGISTRO',
                            loadedTable=tables['TB_REGISTRO'].values
                        ):
        
        response=await self.createTable()
        table=dynamodb.Table(table_name)
        dataset=pd.DataFrame(loadedTable)

        for v in dataset.values:
            dynamoItem={
                "NUM_BO":int(v[0]),
                "ANO_BO":int(v[1]),
                "DATAOCORRENCIA":str(v[2]),
                "HORAOCORRENCIA":str(v[3]),
                "PERIDOOCORRENCIA":str(v[4]),
                "DATACOMUNICACAO":str(v[5]),
                "DATAELABORACAO":str(v[6]),
                "FLAGRANTE":str(v[7]),
                "EXAME":str(v[8]),
                "SOLUCAO":str(v[9]),
                "STATUS":str(v[10])
            }
            
            print(json.dumps(dynamoItem,indent=4,ensure_ascii=False),'\n')
            dumpedItem = json.loads(json.dumps(dynamoItem), parse_float=decimal.Decimal) # Convert float values to Decimal
            
            # Check if the item already exists in the table
            scanTable = table.scan(FilterExpression=Attr('NUM_BO').eq(dynamoItem['NUM_BO']) & Attr('ANO_BO').eq(dynamoItem['ANO_BO']))
            if scanTable['Count'] == 0:
                table.put_item(Item=dumpedItem) # Insert item
            else:
                # The item already exists, ignore it
                print('Item already exists in the table!\nSkipping...\n')


    @classmethod
    async def callDynamoService(self):
        await self.insertItems()


class TB_ENDERECO():
    
    def __init__(self):
        super(TB_ENDERECO.self).__init__()

    @classmethod
    async def callDynamoService(self):
        await self.insertItems()


class TB_VITIMA():
    
    def __init__(self):
        super(TB_VITIMA.self).__init__()

    @classmethod
    async def callDynamoService(self):
        await self.insertItems()


class TB_TELEFONE():
    
    def __init__(self):
        super(TB_TELEFONE.self).__init__()

    @classmethod
    async def callDynamoService(self):
        await self.insertItems()


if __name__ == "__main__":
    asyncio.run(TB_REGISTRO.callDynamoService())
    asyncio.run(TB_ENDERECO.callDynamoService())
    asyncio.run(TB_VITIMA.callDynamoService())
    asyncio.run(TB_TELEFONE.callDynamoService())