from pyspark import HiveContext

from bigdata.lysSparkSession import SparkSessionBase


class BusinessAnalysis(SparkSessionBase):
    SPARK_APP_NAME = 'BusinessAnalysis'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark=self._create_spark_session()

    def run(self):
        hc=HiveContext(self.spark.sparkContext)
        b_df=hc.table('business')
        b_df.show()

if __name__ =='__main__':
    BusinessAnalysis().run()