# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'      # 输入自己数据库的用户名
app.config['MYSQL_DATABASE_PASSWORD'] = '1111'  # 输入自己数据库用户名的密码
app.config['MYSQL_DATABASE_DB'] = 'Dpdb'  # 我们要使用的数据库名字
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # 要使用数据库的网址
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showResult')
def showResult():
    return render_template('showResult.html')


if __name__ == '__main__':
    app.run()
