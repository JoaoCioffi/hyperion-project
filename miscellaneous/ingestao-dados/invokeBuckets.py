from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ETL").getOrCreate() # create a Spark session

class Banks():
    def __init__(self):
        super(Banks,self).__init__()
    
    @classmethod
    def loadBucketContent(self,filePath="./buckets/banks/EnquadramentoInicia_v2.csv"):
        print(f'\n\n~Loading file from {filePath}~\n')
        df=spark.read.csv(filePath,header=True,inferSchema=True,sep=';') # read the CSV file into a DataFrame
        df.show()
        return df

class Complaints():
    def __init__(self):
        super(Complaints,self).__init__()
    
    @classmethod
    def loadBucketContent(self,filePath='./buckets/complaints/geral.csv'):
        print(f'\n\n~Loading file from {filePath}~\n')
        df=spark.read.csv(filePath,header=True,inferSchema=True,sep=';') # read the CSV file into a DataFrame
        df.show()
        return df

class Employees():
    def __init__(self):
        super(Employees,self).__init__()
    
    @classmethod
    def loadBucketContent(self,filePath='./buckets/employees/glassdoor_consolidado_join_match.csv'):
        print(f'\n\n~Loading file from {filePath}~\n')
        df=spark.read.csv(filePath,header=True,inferSchema=True,sep=';') # read the CSV file into a DataFrame
        df.show()
        return df