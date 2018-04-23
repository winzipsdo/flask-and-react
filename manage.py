from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
import sqlite3

app = Flask(__name__,
            template_folder='web/templates',  # 修改templates入口
            static_folder='web/static'  # 修改static入口
            )


@app.route('/', methods=['GET', 'POST'])
def index():
    hello = request.args.get('hello')  # get方法获取前端数据
    print(hello)
    # hello = request.form.get('hello')  # post方法获取前端数据
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


def connect_db():
    """连接到数据库"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


@app.route("/api/test", methods=['GET', 'POST'])
def test():
    data = request.form.get('test')
    return data


if __name__ == '__main__':
    # app.run(host='0.0.0.0')  # 这会让操作系统监听所有公网 IP，让自己变得公开可访问
    # app.debug = True  # 这会让服务器在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器
    app.run(debug=True)
