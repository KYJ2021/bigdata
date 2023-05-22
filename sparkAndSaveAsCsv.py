from pyspark.sql import SparkSession, Window
from pyspark import find_spark_home, HiveContext
from pyspark.sql.functions import year, col, desc, dense_rank

from SparkSessionBase import SparkSessionBase

class Save(SparkSessionBase):
    SPARK_URL = "local[8]"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        df = hc.table('***')
        #spark分析代码
        result = df.select()

        #将结果保存到D:/tables/test_json目录下的一个csv文件
        result.repartition(1)\
            .write.format("csv")\
            .save("file:///D:/tables/test_json")

# XXX 大数据分析代码

if __name__ == '__main__':
    Save().start()
