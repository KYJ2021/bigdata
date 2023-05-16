# 配置Spark
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import DoubleType

os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_261'

spark = SparkSession.builder \
    .appName("Hello spark") \
    .master("local") \
    .getOrCreate()

# spark sql: spark session , rdd: spark context
# rdd = spark.sparkContext.parallelize([('tom', 20),('jerry', 1)])
# df = rdd.toDF(['name', 'age'])
#
# #1. # 打印表头
# df.printSchema()
#
# #2. print rows
# df.show()

# 3. 读取文件创建dataframe
df = spark.read \
    .option('header', True) \
    .csv('dataset/BeijingPM20100101_20151231.csv')

# 1. print schema
df.printSchema()
df.show()

# 2. select
clean_df = df.select('year', 'month', 'day', 'PM_Dongsi')
clean_df.show()

# 3. pm per year
#filter:数据筛选；select：转换为浮点型
result = clean_df \
    .filter("PM_Dongsi != 'NA'") \
    .select('year', col('PM_Dongsi').cast(DoubleType())) \
    .groupBy('year') \
    .avg('PM_Dongsi')

result.show()
