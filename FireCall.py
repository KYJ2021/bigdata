
# python
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, ArrayType, StringType, StructField, IntegerType, BooleanType, FloatType
from pyspark.sql.functions import month
from pyspark.sql.functions import weekofyear
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.stat import Correlation
# Driver
spark = SparkSession \
    .builder \
    .master('local') \
    .appName('HelloSpark') \
    .getOrCreate()

fire_schema = StructType([StructField("CallNumber", IntegerType(), True),
                          StructField("UnitID", StringType(), True),
                          StructField("IncidentNumber", IntegerType(), True),
                          StructField("CallType", StringType(), True),
                          StructField("CallDate", StringType(), True),
                          StructField("WatchDate", StringType(), True),
                          StructField("CallFinalDisposition", StringType(), True),
                          StructField("AvailableDtTm", StringType(), True),
                          StructField("Address", StringType(), True),
                          StructField("City", StringType(), True),
                          StructField("Zipcode", IntegerType(), True),
                          StructField("Battalion", StringType(), True),
                          StructField("StationArea", StringType(), True),
                          StructField("Box", StringType(), True),
                          StructField("OriginalPriority", StringType(), True),
                          StructField("Priority", StringType(), True),
                          StructField("FinalPriority", IntegerType(), True),
                          StructField("ALSUnit", BooleanType(), True),
                          StructField("CallTypeGroup", StringType(), True),
                          StructField("NumAlarms", IntegerType(), True),
                          StructField("UnitType", StringType(), True),
                          StructField("UnitSequenceInCallDispatch", IntegerType(), True),
                          StructField("FirePreventionDistrict", StringType(), True),
                          StructField("SupervisorDistrict", StringType(), True),
                          StructField("Neighborhood", StringType(), True),
                          StructField("Location", StringType(), True),
                          StructField("RowID", StringType(), True),
                          StructField("Delay", FloatType(), True)
                          ]
                         )

df = spark.read.option('header', True).schema(fire_schema).csv('dataset/sf-fire-calls.txt')


# df.select('CallType') \
#     .where(col('CallType').isNotNull() & (year(col('CallDate')) == 2018)) \
#     .distinct().show(truncate=False)
cleaned_df = df.withColumn('IncidentDate', to_timestamp(col('CallDate'), 'MM/dd/yyyy')) \
    .drop('CallDate') \
    .withColumn("OnWatchDate", to_timestamp(col("WatchDate"), "MM/dd/yyyy")) \
    .drop("WatchDate") \
    .withColumn("AvailableDtTS", to_timestamp(col("AvailableDtTm"), "MM/dd/yyyy hh:mm:ss a")) \
    .drop("AvailableDtTm")

#过滤CallType == 'Medical Incident', 并只打印"IncidentNumber", "AvailableDtTm", "CallType" 三个字段
print("过滤CallType == 'Medical Incident', 并只打印\"IncidentNumber\", \"AvailableDtTm\", \"CallType\" 三个字段:")
df.select('IncidentNumber', 'AvailableDtTm', 'CallType') \
    .where("CallType == 'Medical Incident'") \
    .show(truncate=False)

#过滤掉CallType为空的数据，并统计唯一CallType的个数
print("过滤掉CallType为空的数据后，唯一CallType的个数为：")
df.select('CallType') \
    .where(col('CallType').isNotNull()) \
    .agg(countDistinct('CallType')) \
    .show(truncate=False)

#过滤掉CallType为空的数据，显示所有的CallType并去重
print("所有CallType（已去重）为：")
df.select('CallType') \
    .where(col('CallType').isNotNull()) \
    .distinct().show(truncate=False)

#重命名Delay为ResponseDelayedinMins，并过滤出延误大于5分钟的记录，只打印ResponseDelayedinMins字段
print("ResponseDelayedinMins字段（已经过滤延误大于5分钟记录）为：")
df.withColumnRenamed('Delay', 'ResponseDelayedinMins') \
    .where('ResponseDelayedinMins > 5') \
    .select('ResponseDelayedinMins').show(truncate=False)

#转换IncidentDate、OnWatchDate、AvailableDtTS为日期格式，并删除掉行AvailableDtTm
print("切换日期格式后：")
cleaned_df = df.withColumn('IncidentDate', to_timestamp(col('CallDate'), 'MM/dd/yyyy')) \
    .drop('CallDate') \
    .withColumn("OnWatchDate", to_timestamp(col("WatchDate"), "MM/dd/yyyy")) \
    .drop("WatchDate") \
    .withColumn("AvailableDtTS", to_timestamp(col("AvailableDtTm"), "MM/dd/yyyy hh:mm:ss a")) \
    .drop("AvailableDtTm")

cleaned_df.select("IncidentDate", "OnWatchDate", "AvailableDtTS").show(5, True)

#显示所有有事故的年份，并按照年份从小到到排序
print("所有有事故的年份如下：")
cleaned_df.select(year('IncidentDate').alias('year')) \
    .distinct() \
    .orderBy(col('year').asc()) \
    .show(truncate=False)

#过滤CallType为空的记录，并统计每种CallType的类型总数并按照顺序倒排
print("每种CallType的类型总数为（已过滤CallType为空的记录）：")
df.where(col('CallType').isNotNull())\
    .groupby('CallType') \
    .agg(count('CallType').alias('count')) \
    .orderBy(col('count').desc()).show(truncate=False)

#1.	打印2018年份所有的CallType，并去重
print("2018年的所有calltype：")
cleaned_df.select('CallType') \
    .where(col('CallType').isNotNull() & (year('IncidentDate') == 2018)) \
    .distinct().show(truncate=False)

#2.	2018年的哪个月份有最高的火警
# cleaned_df.select(month('IncidentDate').alias('month'), 'CallType') \
#     .where((year('IncidentDate') == 2018)) \
#     .groupBy('month', 'CallType') \
#     .count() \
#     .orderBy(col('count').desc()) \
#     .limit(1)\
#     .show(truncate=False)
##请不要使用上面的代码，版本不够跑不出来
max_month = cleaned_df.select(month('IncidentDate').alias('month'), 'CallType') \
    .where((year('IncidentDate') == 2018)) \
    .groupBy('month', 'CallType') \
    .count() \
    .orderBy(col('count').desc()) \
    .select('month') \
    .first()[0]
print(f"2018年最高的火警月份是{max_month}月。")

# #3.	San Francisco的哪个neighborhood在2018年发生的火灾次数最多？
max_neighborhood = cleaned_df.select('Neighborhood') \
    .where(col('City') == 'San Francisco') \
    .where(year(col('IncidentDate')) == 2018) \
    .groupBy('Neighborhood') \
    .count() \
    .orderBy(col('count').desc()) \
    .select('Neighborhood') \
    .first()[0]

print(f"2018年San Francisco发生火灾次数最多的社区是{max_neighborhood}。")

# #4.	San Francisco的哪个neighborhood在2018年响应最慢？
slowest_neighborhood = cleaned_df.select('Neighborhood', 'Delay') \
    .where(col('City') == 'San Francisco') \
    .where(year(col('IncidentDate')) == 2018) \
    .groupBy('Neighborhood') \
    .agg(avg('Delay').alias('Average Delay'))\
    .orderBy(desc('Average Delay'))\
    .first()[0]
print(f"2018年San Francisco相应最慢的neighborhood是{slowest_neighborhood}。")



# #5.	2018年的哪一周的火警次数最多
max_week = cleaned_df.select(weekofyear('IncidentDate').alias('week')) \
    .where(col('City') == 'San Francisco') \
    .where(year(col('IncidentDate')) == 2018) \
    .groupBy('week') \
    .count() \
    .orderBy(col('count').desc()) \
    .select('week') \
    .first()[0]

print(f"2018年San Francisco发生火灾次数最多的周是第{max_week}周。")

# #6.	“neighborhood“ “zip code“ 和“number of fire calls”有关联（correlation）吗？( Is there a correlation between neighborhood, zip code, and number of fire calls?)
output = df.groupBy("Zipcode").agg({"CallNumber": "count"}).withColumnRenamed("count(CallNumber)", "NumberOfFireCalls")
correlation = output.stat.corr("Zipcode", "NumberOfFireCalls")
print("Correlation coefficient between ZipCode and NumberOfFireCalls is: ", correlation)

#7.	实现使用parquest存储并读取
df2 = spark.read.text("dataset/sf-fire-calls.txt")
df2.write.mode("overwrite").parquet('dataset/sf-fire-calls.parquet')
df2 = spark.read.parquet("dataset/sf-fire-calls.parquet")
