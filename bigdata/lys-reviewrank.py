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
        # 读取数据
        business_df = df.table("business")

        # 定义窗口规范
        window_spec = Window.orderBy(desc("review_count"), desc("stars"), "name")

        # 使用 row_number() 函数生成排名
        rank_df = business_df.select(row_number().over(window_spec).alias("rank"), "name", "stars", "city",
                                     "review_count")

        # 对数据按照 rank, review_count, stars, name 进行排序
        result = rank_df.orderBy("rank", "review_count DESC", "stars DESC", "name")
        result.show()
        #sql格式
        #b_df=df.sql("select row_number() over (order by review_count DESC) as rank,name,stars,city,review_count from business order by review_count DESC,stars DESC,name")

if __name__ =='__main__':
    BusinessAnalysis().run()