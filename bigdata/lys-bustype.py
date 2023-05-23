from pyspark import HiveContext
from pyspark.sql import Window
from pyspark.sql.functions import explode, split, count, col, row_number, desc

from bigdata.lysSparkSession import SparkSessionBase


class BusinessAnalysis(SparkSessionBase):
    SPARK_APP_NAME = 'BusinessAnalysis'
    ENABLE_HIVE_SUPPORT = True
    SPARK_URL = "local[8]"

    def __init__(self):
        self.spark=self._create_spark_session()

    def run(self):
        hc=HiveContext(self.spark.sparkContext)
        return hc

    def typesort(hc):
        df = hc.table('business')
        #对数组组成的类别扩展
        b_df = df.withColumn("categories", split("categories", ",")) \
            .select("business_id", "name", "stars", "review_count", explode("categories").alias("categories"))
        #增加对评论数按类型排名
        b_df = b_df.withColumn("rank1",row_number().over(Window.partitionBy("categories").orderBy(desc("review_count"))))
        #用星级和评论数计算平均参数，并利用该参数按类型排名
        b_df = b_df.withColumn("avg", 0.3*col("stars") / 5.0 + 0.7*col("review_count")/8000)
        b_df = b_df.withColumn("rank2", row_number().over(Window.partitionBy("categories").orderBy(desc("avg"))))
        b_df.show(100)

        b_df.write.format("jdbc").\
            option("url", "jdbc:mysql://192.168.102.105:3306/bigdata").\
            option('driver','com.mysql.jdbc.Driver').\
            option("dbtable", 'bus_type_sort').option("user", "root").\
            option("password", "admin").option('useSSL',False).\
            mode('append').save()



    #求最大评论数
    def previewnum(hc):
        df = hc.table("business")
        b_df = df.select("business_id", "name", "review_count").orderBy(desc("review_count"))
        b_df.show()

if __name__ =='__main__':
    hc=BusinessAnalysis().run()
    BusinessAnalysis.typesort(hc)

