import json

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
    # business_id = request.args.get('business_id', '')
    categories = request.args.get('categories', '')
    orderBy = request.args.get('orderBy', '')
    isLocal = request.args.get('isLocal', '')
    city = request.args.get('city', '')

    # sqlf = f"SELECT * FROM business_sort WHERE business_id = '{business_id}'"
    # print(sqlf)
    # with conn.cursor() as cursor:
    #     cursor.execute(sqlf)
    #     categories_array = cursor.fetchall()
    # print(categories_array)
    # categories=categories_array[0]['categories']

    # 构建查询条件
    filters = []
    if categories:
        categories = categories.replace("'", "''")
        filters.append(f"categories = '{categories}'")
    if isLocal == '0':
        if city:
            filters.append(f"city like '%{city}%'")

    # 构建分页查询
    offset = (page_num - 1) * page_size
    sql = f"SELECT * FROM business_sort"
    if filters:
        sql += " WHERE " + " AND ".join(filters)
    sql += f" ORDER BY {orderBy}"
    sql += f" LIMIT {offset}, {page_size}"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        business_sort = cursor.fetchall()

        cursor.execute("SELECT COUNT(*) FROM business_sort"+" WHERE " + " AND ".join(filters))
        total = cursor.fetchone()['COUNT(*)']

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': business_sort, 'total': total}
    return jsonify(result)
@business_bp.route('/business/review')
def get_review():
    rev_business_id = request.args.get('revBusinessId', '')

    # 构建查询条件
    filters = []
    if rev_business_id:
        filters.append(f"rev_business_id like '%{rev_business_id}%'")
        print(rev_business_id)
    else:
        print('error')
        return 'error'


    sql = f"SELECT * FROM business_review_each_year"
    if filters:
        sql += " WHERE " + " AND ".join(filters)
        sql += "ORDER BY which_year"
    with conn.cursor() as cursor:
        cursor.execute(sql)
        business_review_each_year = cursor.fetchall()
        data=[]
        for row in business_review_each_year:
            print(row)
            data.append({
                'which_year': row['which_year'],
                'count': row['count']
            })
        # cursor.execute("SELECT COUNT(*) FROM business_review_each_year"+" WHERE " + " AND ".join(filters))
        # total = cursor.fetchone()['COUNT(*)']
        # 将查询结果转换为字典格式，并返回给前端
    return jsonify(data)
@business_bp.route('/business/wordcloud')
def get_word_list():
    business_id = request.args.get('business_id', '')

    # 构建查询条件
    filters = []
    if business_id:
        filters.append(f"business_id = '{business_id}'")
        print(business_id)
    else:
        print('error')
        return 'error'

    sql = f"SELECT * FROM ReviewKeywords"
    if filters:
        sql += " WHERE " + " AND ".join(filters)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        res_list = cursor.fetchall()
        res_list = res_list[0]['str_keywords'].split()
        data = []
        i=0
        for item in res_list:
            i+=0.5
            data.append({
                'name': item,
                # 'value': np.floor(0.2*np.exp(-(0.3*i-3))+10)
                'value': 50-0.5*i*i
            })
        # cursor.execute("SELECT COUNT(*) FROM ReviewKeywords"+" WHERE " + " AND ".join(filters))
        # total = cursor.fetchone()['COUNT(*)']
        # 将查询结果转换为字典格式，并返回给前端
    return jsonify(data)
@business_bp.route('/business/tip')
def get_tip():
    business_id = request.args.get('business_id', '')
    # 构建查询条件
    filters = []
    if business_id:
        filters.append(f"business_id = '{business_id}'")
        print(business_id)
    else:
        print('error')
        return 'error'

    sql = f"SELECT * FROM Tip"
    if filters:
        sql += " WHERE " + " AND ".join(filters)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        res_list = cursor.fetchall()
        res_list = res_list[0]['tip_text'].split('&')
        data = []
        for item in res_list:
            data.append({
                'text': item,
            })
        # cursor.execute("SELECT COUNT(*) FROM ReviewKeywords"+" WHERE " + " AND ".join(filters))
        # total = cursor.fetchone()['COUNT(*)']
        # 将查询结果转换为字典格式，并返回给前端
    return jsonify(data)
@business_bp.route('/business/advice')
def get_advice():
    categories_array = request.args.get('categories_array','')
    categories_list = json.loads(categories_array)
    print(categories_list)
    # 构建查询条件
    filters = []
    for categories in categories_list:
        categories = categories.replace("'","''")
        filters.append(f"categories = '{categories}'")

    sql = f"SELECT * FROM Advantages"
    if filters:
        sql += " WHERE " + " OR ".join(filters)
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        res_list = cursor.fetchall()
        print(res_list)
    return jsonify(res_list)