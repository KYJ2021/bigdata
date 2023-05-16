import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, year
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType, BooleanType, FloatType

spark = SparkSession.builder \
    .appName("Hello spark") \
    .master("local") \
    .getOrCreate()

e_df = spark.read.format('jdbc')\
    .option('url', 'jdbc:mysql://192.168.102.99:3306/hr')\
    .option('user', 'root')\
    .option('password', 'admin')\
    .option('dbtable', 'employees')\
    .load()

d_df = spark.read.format('jdbc')\
    .option('url', 'jdbc:mysql://192.168.102.99:3306/hr')\
    .option('user', 'root')\
    .option('password', 'admin')\
    .option('dbtable', 'departments')\
    .load()

e_df.join(d_df, e_df['department_id'] == d_df['department_id'])\
    .select(e_df['first_name'], e_df['last_name'], d_df['department_name']).show()
#jodslcgdhsjlj