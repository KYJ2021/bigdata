from flask import Blueprint, jsonify, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

import pymysql

admin_bp = Blueprint('admin', __name__)
conn = pymysql.connect(
    host='kyj',
    port=3306,
    user='root',
    password='admin',
    db='bigdata',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

@admin_bp.route('/admin/newUser')
def get_count():

    sql = f"SELECT * FROM user_new_register_each_year"
    sql += " ORDER BY year"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        business_sort = cursor.fetchall()

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': business_sort}
    return jsonify(result)
@admin_bp.route('/admin/activity')
def get_rank():
    page_num = request.args.get('pageNum', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    which_year = request.args.get('which_year', '')
    # 构建查询条件
    filters = []
    if which_year:
        filters.append(f"year = '{which_year}'")

    # 构建分页查询
    offset = (page_num - 1) * page_size
    sql = f"SELECT * FROM UserAnnualActivity"
    if filters:
        sql += " WHERE " + " AND ".join(filters)
    sql += " ORDER BY count desc"
    sql += f" LIMIT {offset}, {page_size}"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        business_sort = cursor.fetchall()
        sqlt = "SELECT COUNT(*) FROM UserAnnualActivity"
        if filters:
            sqlt += " WHERE " + " AND ".join(filters)
        print(sqlt)
        cursor.execute(sqlt)
        total = cursor.fetchone()['COUNT(*)']

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': business_sort, 'total': total}
    return jsonify(result)
@admin_bp.route('/admin/typeSort')
def get_type():
    rankBy = request.args.get('rankBy', '')


    sql = f"SELECT categories,{rankBy} FROM type_sort"
    sql += f" ORDER BY {rankBy} desc"
    sql += f" LIMIT 0, 10"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        type_sort = cursor.fetchall()

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': type_sort}
    return jsonify(result)
@admin_bp.route('/admin/areacity')
def get_city():
    rankBy = request.args.get('rankBy', '')

    sql = f"SELECT city,`{rankBy}` FROM city_num"
    sql += f" ORDER BY `{rankBy}` desc"
    sql += f" LIMIT 0, 10"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        type_sort = cursor.fetchall()

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': type_sort}
    return jsonify(result)
@admin_bp.route('/admin/areastate')
def get_state():
    rankBy = request.args.get('rankBy', '')

    sql = f"SELECT state,`{rankBy}` FROM state_num"
    sql += f" ORDER BY `{rankBy}` desc"
    sql += f" LIMIT 0, 10"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        type_sort = cursor.fetchall()

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': type_sort}
    return jsonify(result)
@admin_bp.route('/admin/allstate')
def get_allstate():

    sql = f"SELECT distinct state FROM brand_state"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        type_sort = cursor.fetchall()

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': type_sort}
    return jsonify(result)
@admin_bp.route('/admin/allcity')
def get_allcity():

    sql = f"SELECT distinct city FROM brand_city"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        type_sort = cursor.fetchall()

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': type_sort}
    return jsonify(result)
@admin_bp.route('/admin/brandall')
def get_allbrand():
    rankBy = request.args.get('rankBy', '')
    sql = f"SELECT `name`,`count` FROM brank_all"
    sql += f" order by `count` desc limit 0,18"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        type_sort = cursor.fetchall()
    # 假设您想要将列名old_col1更改为new_col1，将列名old_col2更改为new_col2，将列名old_col3更改为new_col3
    new_col_names = {'name': 'name', 'count': 'value'}
    # 使用列表推导式和字典解析来创建一个新的字典列表，其中包含具有新列名的相同键值对
    new_dicts = [{new_col_names[k]: v for k, v in d.items()} for d in type_sort]

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': new_dicts}
    return jsonify(result)
@admin_bp.route('/admin/brandcity')
def get_citybrand():
    rankBy = request.args.get('rankBy', '')
    sql = f"SELECT `name`,`count` FROM brand_city"
    sql += f" where city = '{rankBy}'"
    sql += f" order by `count` desc limit 0,9"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        type_sort = cursor.fetchall()
    # 假设您想要将列名old_col1更改为new_col1，将列名old_col2更改为new_col2，将列名old_col3更改为new_col3
    new_col_names = {'name': 'name', 'count': 'value'}
    # 使用列表推导式和字典解析来创建一个新的字典列表，其中包含具有新列名的相同键值对
    new_dicts = [{new_col_names[k]: v for k, v in d.items()} for d in type_sort]

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': new_dicts}
    return jsonify(result)
@admin_bp.route('/admin/brandstate')
def get_statebrand():
    rankBy = request.args.get('rankBy', '')
    sql = f"SELECT `name`,`count` FROM brand_state"
    sql += f" where state = '{rankBy}'"
    sql += f" order by `count` desc limit 0,9"
    print(sql)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        type_sort = cursor.fetchall()

    # 假设您想要将列名old_col1更改为new_col1，将列名old_col2更改为new_col2，将列名old_col3更改为new_col3
    new_col_names = {'name': 'name', 'count': 'value'}
    # 使用列表推导式和字典解析来创建一个新的字典列表，其中包含具有新列名的相同键值对
    new_dicts = [{new_col_names[k]: v for k, v in d.items()} for d in type_sort]

    # 将查询结果转换为字典格式，并返回给前端
    result = {'records': new_dicts}
    return jsonify(result)