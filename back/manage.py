from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from blueprints.user import user_bp
from blueprints.business import business_bp
from blueprints.login import login_bp

# 创建 Flask 应用程序实例
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})
# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@hostname/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建 SQLAlchemy 对象
# db = SQLAlchemy(app)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(business_bp)
app.register_blueprint(login_bp)

# 如果是主程序入口，则启动 Flask 应用程序
if __name__ == '__main__':
    app.run(port=9090)