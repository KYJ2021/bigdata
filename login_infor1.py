
import pymysql
from pyspark.sql import SparkSession, Window
from pyspark import find_spark_home, HiveContext
from pyspark.sql.functions import year, col, desc, asc, lit, concat, monotonically_increasing_id
from SparkSessionBase import SparkSessionBase

class TextRandJob(SparkSessionBase):
    SPARK_URL = "local[8]"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc=HiveContext(self.spark.sparkContext)
        u_df=hc.table('users')
        user=u_df.select(col('user_id').alias('id'),col('user_name').alias('nickname')).withColumn('categories', lit('')).withColumn('username',concat(lit('user'),monotonically_increasing_id())).withColumn('userType',lit(1))
        b_df=hc.table('business')
        business=b_df.select(col('business_id').alias('id'),col('name').alias('nickname'), col('categories')).withColumn('username',concat(lit('business'),monotonically_increasing_id())).withColumn('userType', lit(2))
        merge=user.union(business)
        admin_records = self.spark.createDataFrame([(0, "superadmin1", "1", "admin0", 0), (1, "superadmin2", "1", "admin1", 0)], ["id", "nickname", "categories", "username", "userType"])
        result=merge.union(admin_records)
        # merge.show(100)

        result.write.format('jdbc') \
            .option('url', 'jdbc:mysql://192.168.102.105:3306/bigdata') \
            .option('driver', 'com.mysql.jdbc.Driver') \
            .option('dbtable', 'login_information') \
            .option('user', 'root') \
            .option('password', 'admin') \
            .option('useSSL', False) \
            .mode('append') \
            .save()
# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()