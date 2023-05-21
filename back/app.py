#测试前后端是否连通，以及图片能否正常显示
import base64
import io

from flask import Flask, jsonify
import matplotlib.pyplot as plt
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
# 处理跨域问题，前端端口是8080
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

@app.route('/api/plot')
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

if __name__ == '__main__':
    # 后端端口是9090，运行文件时用python ***.py，不要点这个绿色三角运行
    app.run(port=9090)