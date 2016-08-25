# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
import pygal
import dropDown
import graphing

app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'  # 输入自己数据库的用户名
app.config['MYSQL_DATABASE_PASSWORD'] = '1111'  # 输入自己数据库用户名的密码
app.config['MYSQL_DATABASE_DB'] = 'Dpdb'  # 我们要使用的数据库名字
app.config['MYSQL_DATABASE_HOST'] = 'localhost'  # 要使用数据库的网址
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/filterStudent', methods=['GET', 'POST'])
def filterStudent():
    current_coach = request.args.get('choice', 0, type=int)
    try:
        db = mysql.connect()
        cursor = db.cursor()
        try:
            student_list = dropDown.filter(current_coach, cursor)
            return jsonify(student_list=student_list)
        except:
            print "filterStudent - step2 failed."
            print "Error: unable to fetch data"
    except Exception as e:
        print "filterStudent - step1 failed."
        return str(e)
    finally:
        cursor.close()
        db.close()


@app.route('/showResult')
def showResult():
    # show the init result. ave-coach and ave-student
    try:
        db = mysql.connect()
        cursor = db.cursor()
        try:
            coach_info, student_info = dropDown.init(cursor)
            return render_template('showResult.html', coach_info=coach_info, student_info=student_info)

        except:
            print "Error: unable to fetch data"
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    app.run()
