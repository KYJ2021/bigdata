from pyspark.sql import SparkSession, Window
from pyspark import find_spark_home, HiveContext
from pyspark.sql.functions import year, col, lit, row_number, desc, dense_rank

from SparkSessionBase import SparkSessionBase

class RecommendByRecentReview(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc=HiveContext(self.spark.sparkContext)
        re_df=hc.table('review')
        usr_df=hc.table('users')
        w = Window.orderBy(lit(1))
        usr_df=usr_df.withColumn('number','user'+row_number().over(w))
        w1=Window.partitionBy('number').orderBy(col('rev_date').desc())
        result=re_df.join(usr_df,usr_df['user_id']==re_df['rev_user_id']).select('review_id','rev_business_id',dense_rank().over(w1))

# XXX 大数据分析代码

if __name__ == '__main__':
    RecommendByRecentReview().start()