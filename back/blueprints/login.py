import pymysql
from flask import Blueprint, jsonify, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

login_bp = Blueprint('login', __name__)
conn = pymysql.connect(
    host='kyj',
    port=3306,
    user='root',
    password='admin',
    db='bigdata',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)
@login_bp.route('/login', methods=['GET'])
def get_login():
    username = request.args.get('username', '')
    # 构建查询条件
    filters = []
    if username:
        filters.append(f"username = '{username}'")
    sql = f"SELECT * FROM login_information"
    if filters:
        sql += " WHERE " + " AND ".join(filters)
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        user = cursor.fetchall()
    # 将查询结果转换为字典格式，并返回给前端
    result = {'data': user}
    print(result)
    return jsonify(result)
