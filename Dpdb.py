# -*- coding: utf-8 -*-
from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify
from InsertDataFromExcel import insertDataFromExcel
import os
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
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['xls', 'xlsx'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
      filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/upload_homepage')
def upload_homepage():
    return render_template('upload_homepage.html')


# Route that will process the file upload
@app.route('/upload_succeeded', methods=['POST'])
def upload_succeeded():
    try:
        # Get the name of the uploaded files
        uploaded_files = request.files.getlist("file[]")
        filenames = []
        for file in uploaded_files:
            # Check if the file is one of the allowed types/extensions
            if file and allowed_file(file.filename):
                # Make the filename safe, remove unsupported chars
                # filename = secure_filename(file.filename)
                filename = file.filename
                # Move the file form the temporal folder to the upload
                # folder we setup
                file.save(filename)

                # 插入数据,若插入失败,则抛出异常
                insert_ok = insertDataFromExcel(filename)
                if insert_ok != 1:
                    raise insert_ok
                # 上传之后,将文件删除
                os.remove(filename)
                # Save the filename into a list, we'll use it later
                filenames.append(filename)

        # 若没有选择文件点击'上传',则抛出异常
        if not filenames:
            raise Exception('No file is selected.')
        return render_template('upload_succeeded.html', filenames=filenames)
    except Exception, e:
        return render_template('upload_error.html', error=e)


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
            graph_info_date = graphing.draw(cursor, stu_id, stu_text, "date_")
            graph_info_num = graphing.draw(cursor, stu_id, stu_text, "number_")
            return jsonify(graph_info_date = graph_info_date, graph_info_num = graph_info_num)
        except Exception as e:
            print str(e)
            print "drawLines - step2 failed."
    except Exception as e:
        print "drawLines - step1 failed."
        return str(e)
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    app.run()
