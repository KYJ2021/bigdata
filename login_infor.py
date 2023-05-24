
import pymysql
from pyspark.sql import SparkSession, Window
from pyspark import find_spark_home, HiveContext
from pyspark.sql.functions import year, col, desc, asc, lit, concat, monotonically_increasing_id
from SparkSessionBase import SparkSessionBase

from dbutils.pooled_db import PooledDB

class MySQLPool(object):
    __pool = None

    @staticmethod
    def get_conn():
        if MySQLPool.__pool is None:
            MySQLPool.__pool = PooledDB(
                creator=pymysql,  # 使用PyMySQL作为连接池的数据库连接库
                maxconnections=20,  # 连接池允许的最大连接数，根据实际情况进行调整
                host='192.168.102.105',
                user='root',
                password='admin',
                db='bigdata',
                port=3306,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )
        return MySQLPool.__pool.connection()

class TextRandJob(SparkSessionBase):
    SPARK_URL = "local[8]"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc=HiveContext(self.spark.sparkContext)
        u_df = hc.table('users')
        user = u_df.select(col('user_id').alias('id'), col('user_name').alias('nickname')).withColumn('categories', lit('')).withColumn('username', concat(lit('user'), monotonically_increasing_id())).withColumn('userType',lit(1))
        b_df = hc.table('business')
        business = b_df.select(col('business_id').alias('id'), col('name').alias('nickname'),col('categories')).withColumn('username', concat(lit('business'),monotonically_increasing_id())).withColumn('userType', lit(2))
        merge = user.union(business)
        admin_records = self.spark.createDataFrame(
            [(0, "superadmin1", "null", "admin0", 0), (1, "superadmin2", "null", "admin1", 0)],
            ["id", "nickname", "categories", "username", "userType"])
        result = merge.union(admin_records)
        # merge.show(100)

        # 使用连接池写入数据：
        # 创建MySQL连接池
        pool = MySQLPool.get_conn()

        # 将DataFrame转换为Python List
        data = result.collect()

        try:
            # 获取MySQL连接
            conn = pool.cursor()
            # 批量插入数据
            sql = "INSERT INTO login_information (id, nickname, categories, username, userType) VALUES (%s, %s, %s, %s, %s)"
            values = [(row['id'], row['nickname'], row['categories'], row['username'], row['userType']) for row in data]
            conn.executemany(sql, values)
            # 提交事务
            pool.commit()
            print("数据写入成功！")
        except Exception as e:
            # 回滚事务
            pool.rollback()
            print("数据写入失败！", e)
        finally:
            # 关闭连接
            print("end")
            conn.close()
            pool.close()
# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()