import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, year, split, explode
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType, BooleanType, FloatType, Row

spark = SparkSession.builder \
    .appName("Hello spark") \
    .master("local") \
    .getOrCreate()

# 1. map
# rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
#
# result = rdd.map(lambda x: x * x)
#
# print(result.collect())

# 2. flat map
# df = spark.read.text('AdvancedFunctions.py')
# df.withColumn('words', split(col('value'),  ' '))\
#     .select(explode(col('words')).alias('word'))\
#     .groupBy('word')\
#     .count().show()

# 3. filter
# rdd = spark.sparkContext.parallelize([('tom', 40), ('jack', 18)])
# df = rdd.toDF(['name', 'age'])
#
# df.filter(col('age') < 20).show()
# df.filter("age < 20").show()
#
# df.where(col('age') < 20).show()

# 4. order by
# rdd = spark.sparkContext.parallelize([("jayChou", 41), ("burukeyou", 23), ("jack", 30)])
#
# df = spark.createDataFrame(rdd.map(lambda row: Row(name=row[0], age=row[1])))
#
# df.orderBy(col('age').asc()).show()
# df.sort()

# 5. 类型转换
rdd = spark.sparkContext.parallelize([("jayChou", 41), ("burukeyou", 23), ("jack", 30)])

df = spark.createDataFrame(rdd.map(lambda row: Row(name=row[0], age=row[1])))

df.printSchema()

df.select('name', col('age').cast(StringType())).printSchema()