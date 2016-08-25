# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
import dropDown
import pygal
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

@app.route('/showResult')
def showResult():
    """ author: Lyu
    show the init result. ave-coach and ave-student """
    try:
        db = mysql.connect()
        cursor = db.cursor()
        try:
            coach_info, student_info = dropDown.init(cursor)
            graph_info = graphing.init()
            return render_template('showResult.html', coach_info=coach_info, student_info=student_info, graph_info = graph_info)

        except:
            print "Error: unable to fetch data"
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        db.close()

@app.route('/filterStudent')
def filterStudent():
    """ author: Lyu
    filter student range according to the coach selected.
    """
    current_coach = request.args.get('choice', 0, type=int)
    try:
        db = mysql.connect()
        cursor = db.cursor()
        try:
            student_list = dropDown.filter(cursor, current_coach)
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

@app.route('/drawLines')
def drawLines():
    """ author: Lyu
        draw lines of 7 indexes for the selected student.
    """
    stu_id = request.args.get('stu_id', 0, type=int)
    stu_text = request.args.get('stu_text')
    print stu_id, stu_text
    try:
        db = mysql.connect()
        cursor = db.cursor()
        try:
            graph_info = graphing.draw(cursor, stu_id, stu_text)
            return jsonify(graph_info=graph_info)
        except:
            print "drawLines - step2 failed."
    except Exception as e:
        print "drawLines - step1 failed."
        return str(e)
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    app.run()
