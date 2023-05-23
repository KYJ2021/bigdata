from flask import Blueprint, jsonify, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

import pymysql

business_bp = Blueprint('business', __name__)
conn = pymysql.connect(
    host='kyj',
    port=3306,
    user='root',
    password='admin',
    db='bigdata',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

@business_bp.route('/business/rank/type')
def get_rank():
    page_num = request.args.get('pageNum', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    categories = request.args.get('categories', '')

    # 构建查询条件
    filters = []
    if categories:
        filters.append(f"categories like '%{categories}%'")

    # 构建分页查询
    offset = (page_num - 1) * page_size
    sql = f"SELECT * FROM bus_type_sort"
    if filters:
        sql += " WHERE " + " AND ".join(filters)
    sql += f" LIMIT {offset}, {page_size}"
    with conn.cursor() as cursor:
        cursor.execute(sql)
        bus_type_sort = cursor.fetchall()

        cursor.execute("SELECT COUNT(*) FROM bus_type_sort"+" WHERE " + " AND ".join(filters))
        total = cursor.fetchone()['COUNT(*)']

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': bus_type_sort, 'total': total}
    return jsonify(result)
