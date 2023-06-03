from pyspark.sql import SparkSession
import argparse

def generateSparkEnv(data_source='./Food_Establishment_Inspection_Data.csv'):
    with SparkSession.builder.appName("Calculate Red Health Violations").getOrCreate() as spark:
        if data_source is not None:
            source_df = spark.read.option("header", "true").csv(data_source)
        
        # Create an in-memory DataFrame to query
        source_df.createOrReplaceTempView("restaurant_violations")

        # Create a DataFrame of the top 10 restaurants with the most Red violations
        top_red_violation_restaurants = spark.sql("""
          SELECT inspection_business_name, count(*) AS total_red_violations 
          FROM restaurant_violations 
          WHERE violation_type = 'RED' 
          GROUP BY inspection_business_name 
          ORDER BY total_red_violations DESC LIMIT 10
          """)
        top_red_violation_restaurants.write.option("header", "true").mode("overwrite").csv('./logs/top-10-restaurants-step')

        # Create a DataFrame of the top 10 cities with the most Red violations
        top_red_violation_cities = spark.sql("""
          SELECT city, count(*) AS total_red_violations
          FROM restaurant_violations 
          WHERE violation_type = 'RED' 
          GROUP BY city 
          ORDER BY total_red_violations DESC LIMIT 10
        """)
        top_red_violation_cities.write.option("header", "true").mode("overwrite").csv('./logs/top-10-cities-step')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_source', help="The URI for you CSV restaurant data, like an S3 bucket location.")
    parser.add_argument(
        '--output_uri', help="The URI where output is saved, like an S3 bucket location.")
    args = parser.parse_args()
    generateSparkEnv()
