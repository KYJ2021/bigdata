from pyspark.sql import SparkSession, Window
from pyspark import find_spark_home, HiveContext
from pyspark.sql.functions import year, col, lit, row_number, desc, dense_rank, to_timestamp

from SparkSessionBase import SparkSessionBase

class RecommendByRecentReview(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc=HiveContext(self.spark.sparkContext)
        re_df=hc.table('review').limit(50000)
        w1=Window.partitionBy('rev_user_id').orderBy(col('rev_date').desc())
        result=re_df.select('rev_user_id','review_id','rev_business_id','rev_date',dense_rank().over(w1))
        result.show()
# XXX 大数据分析代码

if __name__ == '__main__':
    RecommendByRecentReview().start()