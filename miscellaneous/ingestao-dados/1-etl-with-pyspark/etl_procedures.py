import asyncio 
#import trio
from invokeBuckets import Banks,\
                          Complaints,\
                          Employees
from pyspark.sql import SparkSession
import pandas as pd
spark = SparkSession.builder.appName("ETL")\
                            .config("spark.sql.debug.maxToStringFields", 100)\
                            .getOrCreate() # create a Spark session

class ETL():
    def __init__(self):
        super(ETL,self).__init__()
    
    @classmethod
    async def extractionStage(self):
        print('\n\n#-----[Extraction Stage]-----#\n')
        df_banks=Banks.loadBucketContent()
        df_complaints=Complaints.loadBucketContent()
        df_employees=Employees.loadBucketContent()
        return df_banks,\
               df_complaints,\
               df_employees # returns raw dataframes
    
    @classmethod
    async def transformationStage(self):
        
        df_banks,df_complaints,df_employees=await self.extractionStage() # calling previous method/function

        print('\n\n#-----[Transformation Stage]-----#\n')

        # drop NaN
        df_banks=df_banks.na.drop(subset=['cnpj'])
        df_complaints=df_complaints.na.drop(subset=['cnpj'])
        df_banks=df_banks.na.drop(subset=['cnpj'])

        # join tables and add suffixes
        df_joined=df_banks.join(df_complaints,on='cnpj',how='inner').join(df_employees,on='cnpj',how='inner')
        
        print(df_joined.columns,'\n\n')

        # select fields
        # desiredFields=['nome',
        #                'cnpj',
        #                'qtd_total_clientes_ccs_e_scr',
        #                'indice',
        #                'qtd_total_reclamacoes',
        #                'recomendam_para_outras_pessoas_percent',
        #                'remuneracao_e_beneficios']
        # finalTable=df_joined.select(*desiredFields)
        print('\n\n#-----[Load Stage]-----#\n')
        finalTable=pd.DataFrame(df_joined.toPandas())
        print(finalTable.head())
        return finalTable
    
    @classmethod
    async def loadStage(self):
        finalTable=await self.transformationStage()

        print('\n\n#-----[Load Stage]-----#\n')

        # saving file locally (in memory)
        outputFilePath='./buckets/final_stage'
        # Save the DataFrame as a CSV file in the specified output folder
        # The coalesce(1) is used to write the output as a single CSV file
        finalTable.to.csv(outputFilePath)

# ETL.extractionStage()
asyncio.run(ETL.transformationStage())
spark.stop()