from soda.scan import Scan
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("ETL").getOrCreate() # create a Spark session

df=spark.read.csv("./data/banks/EnquadramentoInicia_v2.csv",header=True,inferSchema=True,sep=';') # read the CSV file into a DataFrame

df.createOrReplaceTempView("banks")

scan = Scan()
scan.set_scan_definition_name('local-schedule-pyspark')
scan.set_data_source_name("spark_df")
scan.add_configuration_yaml_str(
    """
soda_cloud:
  # use cloud.soda.io for EU region; use cloud.us.soda.io for USA region
  host: cloud.us.soda.io
  api_key_id: "45042cdb-2112-44cb-8e37-9f8426581f13"
  api_key_secret: "kN4WMkz72SSaT0LtDxGgsmsOxL1YmOKJjtx3e7dsBRA-hfslHNphnA"
"""
)
scan.add_spark_session(spark)
scan.execute()

# print(scan.get_all_checks_text())
print(scan.get_logs_text())
# scan.assert_no_checks_fail()