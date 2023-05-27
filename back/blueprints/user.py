import pymysql
from flask import Blueprint, jsonify, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

user_bp = Blueprint('user', __name__)
conn = pymysql.connect(
    host='kyj',
    port=3306,
    user='root',
    password='admin',
    db='bigdata',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

@user_bp.route('/user/friend')
def get_friend():
    user = request.args.get('user', '')
    # 构建查询条件
    filters = []
    if user:
        filters.append(f"`user` = '{user}'")
        print(user)
    else:
        print('error')
        return 'error'

    sql = f"SELECT * FROM friend_recommend"
    if filters:
        sql += " WHERE " + " AND ".join(filters)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        res_list = cursor.fetchall()
        res_list = res_list[0]['friends'].split(',')
        data = []
        for item in res_list:
            data.append({
                'friend_id': item.split(':')[0],
                'friend_name': item.split(':')[1],
                'fans': item.split(':')[2],
                'rewards': item.split(':')[3]
            })
        # cursor.execute("SELECT COUNT(*) FROM ReviewKeywords"+" WHERE " + " AND ".join(filters))
        # total = cursor.fetchone()['COUNT(*)']
        # 将查询结果转换为字典格式，并返回给前端
    return jsonify(data)