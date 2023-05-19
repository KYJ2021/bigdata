from pyspark import HiveContext
from pyspark.sql import Window
from pyspark.sql.functions import row_number, desc
from bigdata.lysSparkSession import SparkSessionBase


class BusinessAnalysis(SparkSessionBase):
    SPARK_APP_NAME = 'BusinessAnalysis'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark=self._create_spark_session()

    def run(self):
        df=HiveContext(self.spark.sparkContext)
        df = df.table('business')
        result = (df.groupBy("city")
                  .agg(sum("review_count").alias("tot"))
                  .withColumn("rank", row_number().over(Window.orderBy(desc("tot"))))
                  .select("rank", "city", "tot")
                  .orderBy(desc("tot")))
        result.show()
        #sql
        #cityrank(byreview) = hc.sql("select row_number() over (order by sum(review_count) DESC) as rank,city,sum(review_count) as tot from business group by city order by tot desc")
if __name__ =='__main__':
    BusinessAnalysis().run()