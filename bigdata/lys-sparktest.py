from pyspark import HiveContext

from bigdata.lysSparkSession import SparkSessionBase


class BusinessAnalysis(SparkSessionBase):
    SPARK_APP_NAME = 'BusinessAnalysis'
    ENABLE_HIVE_SUPPORT = True
    SPARK_URL = "local[8]"

    def __init__(self):
        self.spark=self._create_spark_session()

    def run(self):
        hc=HiveContext(self.spark.sparkContext)
        b_df=hc.table('business')
        b_df.show()

if __name__ =='__main__':
    BusinessAnalysis().run()

# %jdbc
# mysql_url = "jdbc:mysql://localhost:3306/interview"
# username = "root"
# password = "123"
# driver = "com.mysql.jdbc.Driver"
# b_df.write.jdbc(url=mysql_url, table="cityrankbyreview", mode="overwrite", properties={"user":username, "password":password, "driver":driver})