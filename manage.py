from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from src.Models.Daily import daily_tasks

app = Flask(__name__,
            template_folder='web/spider/build',  # 修改templates入口
            static_folder='web/spider/build/static'  # 修改static入口
            )

# 数据库配置
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:123@localhost/lenovo'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    hello = request.args.get('hello')  # get方法获取前端数据
    if hello:
        print(hello)
    # hello = request.form.get('hello')  # post方法获取前端数据
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.route("/api/test", methods=['GET', 'POST'])
def test():
    data = request.form.get('test')
    return data


@app.route("/api/laptops", methods=['POST'])
def get_laptops():
    site = request.form.get('site')
    return site


if __name__ == '__main__':
    # app.run(host='0.0.0.0')  # 这会让操作系统监听所有公网 IP，让自己变得公开可访问
    # app.debug = True  # 这会让服务器在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器
    app.run(debug=True)
    # daily_tasks()  # 每日自动爬取的实现
