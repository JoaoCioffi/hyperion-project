from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError
from data_source import loadData
from datetime import datetime
import matplotlib.pyplot as plt
import statistics as st
import pandas as pd
import env
import boto3
import json
import asyncio
import decimal
import time

env=env.environment()
tables=loadData.tablesGenerator()
dynamodb=boto3.resource(
                            "dynamodb",
                            region_name=env['aws-region'],
                            endpoint_url=env['endpoint-url'],
                            aws_access_key_id=env['aws-access-key-id'], 
                            aws_secret_access_key=env['aws-secret-access-key']
                        ) # Connect to local instance

performance = {
    'insertionElapsedTime':{
        'TB_REGISTRO':[],
        'TB_ENDERECO':[],
        'TB_VITIMA':[],
        'TB_TELEFONE':[]
    },
    'avgInsertionRate':{
        'TB_REGISTRO':[],
        'TB_ENDERECO':[],
        'TB_VITIMA':[],
        'TB_TELEFONE':[]
    },
    'insertedItems':{
        'TB_REGISTRO':[],
        'TB_ENDERECO':[],
        'TB_VITIMA':[],
        'TB_TELEFONE':[]
    }
}

class TB_REGISTRO():
    
    def __init__(self):
        print('_'*35)
        print("\n.::. [TB_REGISTRO] .::.")
        print('_'*35)
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
                print('\n>> Table already exists, skipping...\n')
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
        counter=0

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

            print('-='*30,'\n')
            print(json.dumps(dynamoItem,indent=4,ensure_ascii=False),'\n')
            dumpedItem = json.loads(json.dumps(dynamoItem), parse_float=decimal.Decimal) # Convert float values to Decimal
            
            # Checks if the item already exists in the table
            scanTable = table.scan(FilterExpression=Attr('NUM_BO').eq(dynamoItem['NUM_BO']) & Attr('ANO_BO').eq(dynamoItem['ANO_BO']))
            if scanTable['Count'] == 0:
                t0=time.time()
                table.put_item(Item=dumpedItem) # Insert item
                counter+=1
                tf=time.time()
                dt=tf-t0
                avg=1/dt

                print(f'\n>> Current Avg Insertion Rate ~ {round(avg,4)} items/sec in a total of {counter} iserted items...\n')

                performance['insertionElapsedTime']['TB_REGISTRO'].append(dt)
                performance['avgInsertionRate']['TB_REGISTRO'].append(avg)
                performance['insertedItems']['TB_REGISTRO'].append(counter)
                
                del t0,tf,dt,avg
            else:
                # The item already exists, ignore it
                print('\n>> Item already exists in the table!\nSkipping...\n')
        del counter

    @classmethod
    async def callDynamoService(self):
        await self.insertItems()


class TB_ENDERECO():
    
    def __init__(self):
        print('_'*35)
        print("\n.::. [TB_ENDERECO] .::.")
        print('_'*35)
        super(TB_ENDERECO.self).__init__()
    
    @classmethod
    async def createTable(self,table_name='TB_ENDERECO'):

        # table attributes
        attribute_definitions=[
            {
                'AttributeName': 'NUM_BO',
                'AttributeType': 'N'
            }
        ]

        # table primary keys
        key_schema=[
            {
                'AttributeName': 'NUM_BO',
                'KeyType': 'HASH'  # partition key
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
                print('\n>> Table already exists, skipping...\n')
            else:
                return e
    
    @classmethod
    async def insertItems(
                            self,
                            table_name='TB_ENDERECO',
                            loadedTable=tables['TB_ENDERECO'].values
                        ):
        counter=0
        await self.createTable()
        table=dynamodb.Table(table_name)
        dataset=pd.DataFrame(loadedTable)

        for v in dataset.values:
            dynamoItem={
                "NUM_BO":int(v[0]),
                "LOGRADOURO":str(v[1]),
                "NUMERO":str(v[2]),
                "BAIRRO":str(v[3]),
                "CIDADE":str(v[4]),
                "UF":str(v[5]),
                "DESCRICAOLOCAL":str(v[6]),
                "DELEGACIANOME":str(v[7])
            }

            print('-='*30,'\n')
            print(json.dumps(dynamoItem,indent=4,ensure_ascii=False),'\n')
            dumpedItem = json.loads(json.dumps(dynamoItem), parse_float=decimal.Decimal) # Convert float values to Decimal

            # Checks if the item already exists in the table
            scanTable = table.scan(FilterExpression=Attr('NUM_BO').eq(dynamoItem['NUM_BO']))
            if scanTable['Count'] == 0:
                t0=time.time()
                table.put_item(Item=dumpedItem) # Insert item
                counter+=1
                tf=time.time()
                dt=tf-t0
                avg=1/dt

                print(f'\n>> Current Avg Insertion Rate ~ {round(avg,4)} items/sec in a total of {counter} iserted items...\n')

                performance['insertionElapsedTime']['TB_ENDERECO'].append(dt)
                performance['avgInsertionRate']['TB_ENDERECO'].append(avg)
                performance['insertedItems']['TB_ENDERECO'].append(counter)
                
                del t0,tf,dt,avg
            else:
                # The item already exists, ignore it
                print('\n>> Item already exists in the table!\nSkipping...\n')
        del counter

    @classmethod
    async def callDynamoService(self):
        await self.insertItems()


class TB_VITIMA():
    
    def __init__(self):
        print('_'*35)
        print("\n.::. [TB_VITIMA] .::.")
        print('_'*35)
        super(TB_VITIMA.self).__init__()
    
    @classmethod
    async def createTable(self,table_name='TB_VITIMA'):

        # table attributes
        attribute_definitions=[
            {
                'AttributeName': 'NUM_BO',
                'AttributeType': 'N'
            }
        ]

        # table primary keys
        key_schema=[
            {
                'AttributeName': 'NUM_BO',
                'KeyType': 'HASH'  # partition key
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
                print('\n>> Table already exists, skipping...\n')
            else:
                return e
        
    @classmethod
    async def insertItems(
                            self,
                            table_name='TB_VITIMA',
                            loadedTable=tables['TB_VITIMA'].values
                        ):
        
        response=await self.createTable()
        table=dynamodb.Table(table_name)
        dataset=pd.DataFrame(loadedTable)
        counter=0

        for v in dataset.values:
            dynamoItem={
                "NUM_BO":int(v[0]),
                "TIPOPESSOA":str(v[1]),
                "VITIMAFATAL":str(v[2]),
                "NACIONALIDADE":str(v[3]),
                "SEXO":str(v[4]),
                "DATANASCIMENTO":str(v[5]),
                "IDADE":str(v[6]),
            }

            print('-='*30,'\n')
            print(json.dumps(dynamoItem,indent=4,ensure_ascii=False),'\n')
            dumpedItem = json.loads(json.dumps(dynamoItem), parse_float=decimal.Decimal) # Convert float values to Decimal

            # Checks if the item already exists in the table
            scanTable = table.scan(FilterExpression=Attr('NUM_BO').eq(dynamoItem['NUM_BO']))
            if scanTable['Count'] == 0:
                t0=time.time()
                table.put_item(Item=dumpedItem) # Insert item
                counter+=1
                tf=time.time()
                dt=tf-t0
                avg=1/dt

                print(f'\n>> Current Avg Insertion Rate ~ {round(avg,4)} items/sec in a total of {counter} iserted items...\n')

                performance['insertionElapsedTime']['TB_VITIMA'].append(dt)
                performance['avgInsertionRate']['TB_VITIMA'].append(avg)
                performance['insertedItems']['TB_VITIMA'].append(counter)
                
                del t0,tf,dt,avg
            else:
                # The item already exists, ignore it
                print('\n>> Item already exists in the table!\nSkipping...\n')
        del counter

    @classmethod
    async def callDynamoService(self):
        await self.insertItems()


class TB_TELEFONE():
    
    def __init__(self):
        print('_'*35)
        print("\n.::. [TB_TELEFONE] .::.")
        print('_'*35)
        super(TB_TELEFONE.self).__init__()
    
    @classmethod
    async def createTable(self,table_name='TB_TELEFONE'):

        # table attributes
        attribute_definitions=[
            {
                'AttributeName': 'NUM_BO',
                'AttributeType': 'N'
            }
        ]

        # table primary keys
        key_schema=[
            {
                'AttributeName': 'NUM_BO',
                'KeyType': 'HASH'  # partition key
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
                print('\n>> Table already exists, skipping...\n')
            else:
                return e
        
    @classmethod
    async def insertItems(
                            self,
                            table_name='TB_TELEFONE',
                            loadedTable=tables['TB_TELEFONE'].values
                        ):
        
        response=await self.createTable()
        table=dynamodb.Table(table_name)
        dataset=pd.DataFrame(loadedTable)
        counter=0

        for v in dataset.values:
            dynamoItem={
                "NUM_BO":int(v[0]),
                "ANO_FABRICACAO":str(v[1]),
                "ANO_MODELO":str(v[2]),
                "QUANT_CELULAR":str(v[3]),
                "MARCA_CELULAR":str(v[4])
            }

            print('-='*30,'\n')
            print(json.dumps(dynamoItem,indent=4,ensure_ascii=False),'\n')
            dumpedItem = json.loads(json.dumps(dynamoItem), parse_float=decimal.Decimal) # Convert float values to Decimal

            # Checks if the item already exists in the table
            scanTable = table.scan(FilterExpression=Attr('NUM_BO').eq(dynamoItem['NUM_BO']))
            if scanTable['Count'] == 0:
                t0=time.time()
                table.put_item(Item=dumpedItem) # Insert item
                counter+=1
                tf=time.time()
                dt=tf-t0
                avg=1/dt

                print(f'\n>> Current Avg Insertion Rate ~ {round(avg,4)} items/sec in a total of {counter} iserted items...\n')

                performance['insertionElapsedTime']['TB_TELEFONE'].append(dt)
                performance['avgInsertionRate']['TB_TELEFONE'].append(avg)
                performance['insertedItems']['TB_TELEFONE'].append(counter)
                
                del t0,tf,dt,avg
            else:
                # The item already exists, ignore it
                print('\n>> Item already exists in the table!\nSkipping...\n')
        del counter

    @classmethod
    async def callDynamoService(self):
        await self.insertItems()

if __name__ == "__main__":

    begin_timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tic=time.time()
    
    asyncio.run(TB_REGISTRO.callDynamoService())
    asyncio.run(TB_ENDERECO.callDynamoService())
    asyncio.run(TB_VITIMA.callDynamoService())
    asyncio.run(TB_TELEFONE.callDynamoService())
    
    toc=time.time()
    end_timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sumAvgs = \
            st.mean(performance['avgInsertionRate']['TB_REGISTRO']) + \
            st.mean(performance['avgInsertionRate']['TB_ENDERECO']) + \
            st.mean(performance['avgInsertionRate']['TB_VITIMA']) + \
            st.mean(performance['avgInsertionRate']['TB_TELEFONE'])

    globalAvg=(1/4)*sumAvgs

    print('_'*35)
    print("\n[TASK FINISHED]")
    print('_'*35)

    print(f'\nProcess started on [{begin_timestamp}] and terminated on [{end_timestamp}]')
    print(f'Total elapsed time is {round(toc-tic,4)}s')
    print(f'Global Avg Insertion Rate ~ {round(globalAvg,4)} items/sec\n')

    # graphical analysis
    fig,axs=plt.subplots(2, 1, figsize=(8, 8))
    axs[0].set_title('Insertion Elapsed Time')
    axs[0].plot(performance['insertionElapsedTime']['TB_REGISTRO'],color='red',label='TB_REGISTRO',linestyle='-',linewidth=0.5)
    axs[0].plot(performance['insertionElapsedTime']['TB_ENDERECO'],color='green',label='TB_ENDERECO',linestyle='--',linewidth=0.5)
    axs[0].plot(performance['insertionElapsedTime']['TB_VITIMA'],color='blue',label='TB_VITIMA',linestyle='-.',linewidth=0.5)
    axs[0].plot(performance['insertionElapsedTime']['TB_TELEFONE'],color='purple',label='TB_TELEFONE',linestyle=':',linewidth=0.5)
    axs[0].set_xlabel('inserted items')
    axs[0].set_ylabel('[s]')
    axs[0].legend()

    axs[1].set_title('Average Insertion Rate')
    axs[1].plot(performance['avgInsertionRate']['TB_REGISTRO'],color='red',label='TB_REGISTRO',linestyle='-',linewidth=0.5)
    axs[1].plot(performance['avgInsertionRate']['TB_ENDERECO'],color='green',label='TB_ENDERECO',linestyle='--',linewidth=0.5)
    axs[1].plot(performance['avgInsertionRate']['TB_VITIMA'],color='blue',label='TB_VITIMA',linestyle='-.',linewidth=0.5)
    axs[1].plot(performance['avgInsertionRate']['TB_TELEFONE'],color='purple',label='TB_TELEFONE',linestyle=':',linewidth=0.5)
    axs[1].set_xlabel('inserted items')
    axs[1].set_ylabel('[items/s]')
    axs[1].legend()

    plt.tight_layout()
    plt.show()

    del begin_timestamp,tic,toc,end_timestamp,sumAvgs,globalAvg,fig,axs