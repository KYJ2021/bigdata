from pyspark.sql import SparkSession
from pyspark import find_spark_home, HiveContext
from pyspark.sql.functions import year, col, desc

from SparkSessionBase import SparkSessionBase

class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc=HiveContext(self.spark.sparkContext)
        #hc = HiveContext(sc)
        re_df = hc.table('review')
        result = re_df.groupby('rev_business_id').count().orderBy(desc('count'))
        result.show()

# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()
