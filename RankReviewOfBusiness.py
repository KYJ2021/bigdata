from pyspark.sql import SparkSession, Window
from pyspark import find_spark_home, HiveContext
from pyspark.sql.functions import year, col, desc

from SparkSessionBase import SparkSessionBase

class RankReviewOfBusiness(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc=HiveContext(self.spark.sparkContext)
        #hc = HiveContext(sc)
        hc = HiveContext(self.spark.sparkContext)
        re_df = hc.table('review')
        w1 = Window.partitionBy('rev_business_id').orderBy('year')
        result = re_df.withColumn('year', year('rev_date')).groupBy('year', 'rev_business_id').count().withColumn('no.',dense_rank().over(w1))
        result.show()

# XXX 大数据分析代码

if __name__ == '__main__':
    RankReviewOfBusiness().start()
