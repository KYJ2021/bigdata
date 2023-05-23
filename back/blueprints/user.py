from flask import Blueprint, jsonify
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def get_plot():
    # 生成图表数据
    x = np.linspace(0.0, 10.0, 100)
    y = np.sin(x)

    # 绘制图表
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # 将图表转换为PNG格式的图像数据
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()

    # 将图像数据以JSON格式返回
    response_data = {'image': base64.b64encode(image_data).decode('utf-8')}
    return jsonify(response_data)

@user_bp.route('/users/<int:user_id>')
def get_user(user_id):
    return f'Get user {user_id}'