# -*- coding: utf-8 -*-
from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify
from InsertDataFromExcel import insertDataFromExcel
import os
import pygal
import dropDown
import graphing
import showAndDelete

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
    try:
        db = mysql.connect()
        cursor = db.cursor()
        try:
            coach_info, student_info = dropDown.init(cursor)
            return render_template('upload_homepage.html', coach_info=coach_info, student_info=student_info)
        except:
            print "Error: unable to fetch data"
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        db.close()


# Route that will process the file upload
@app.route('/upload_result', methods=['POST'])
def upload_result():
    file_succeed = []
    file_failed = []
    error_failed = {}
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
                    file_failed.append(filename)
                    error_failed[filename] = insert_ok
                    # raise insert_ok
                else:
                    file_succeed.append(filename)
                # 上传之后,将文件删除
                os.remove(filename)
                # Save the filename into a list, we'll use it later
                filenames.append(filename)

        # 若没有选择文件点击'上传',则抛出异常
        if not filenames:
            raise Exception('No file is selected.')
    except Exception, e:
        return render_template('upload_error.html', error=e)
    return render_template('upload_succeeded.html', filenames=filenames,
                           file_succeed=file_succeed, file_failed=file_failed,
                           error_failed=error_failed)


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


@app.route('/showItems')
def showItems():
    """ author: Luo
        show Items according to coach_id and stu_id selected
    """
    row_index = [u'教练ID', u'学员ID', u'日期', u'课程次数', u'体重（kg）',
                 u'血压（高压）mmgh（运动前）', u'血压（低压）mmgh（运动前）',
                 u'心率（次/min）', u'体脂（胸、三头）mm', u'体脂（腹、髂）mm',
                 u'体脂（大腿）mm', u'体脂含量%', u'胸围（最高处）cm',
                 u'腰围（肚脐处）cm', u'臀围cm', u'腰臀比', u'大臂围cm', u'大腿围cm',
                 u'小腿围cm', u'推（俯卧撑）次', u'拉（trx或引体向上）次',
                 u'蹲（静蹲）s', u'核心（平板支撑）s', u'平衡（左）s', u'平衡（右）s']
    stu_id = request.args.get('stu_id', 0, type=int)
    coach_id = request.args.get('coach_id', 0, type=int)
    stu_text = request.args.get('stu_text')
    print stu_id, stu_text
    try:
        db = mysql.connect()
        cursor = db.cursor()
        try:
            selected_items = showAndDelete.selectItemsFromLesson(cursor, coach_id, stu_id)
            item_no = len(selected_items)
            return jsonify(selected_items=selected_items, item_no=item_no, row_index=row_index)
        except Exception as e:
            print str(e)
            print "drawLines - step2 failed."
    except Exception as e:
        print "drawLines - step1 failed."
        return str(e)
    finally:
        cursor.close()
        db.close()


@app.route('/updateData')
def updateData():
    update_data = request.args.get('update_data')
    delete_id = request.args.get('delete_id')
    data_list = []

    print data_list
    try:
        db = mysql.connect()
        cursor = db.cursor()
        try:
            if update_data:
                print 'update_data'
                raw_data_list = update_data.split(',')
                for row in raw_data_list:
                    row_list = row.split('&')
                    for i in range(len(row_list)):
                        temp = row_list[i].split('=')
                        if len(temp) == 2:
                            row_list[i] = temp[1]
                    data_list.append(row_list)  # 需要递交修改的行内容

                for i in range(len(data_list)):
                    for j in range(4):
                        del data_list[i][1]  # 只上传后四项内容
                    for j in range(len(data_list[i])):
                        if not data_list[i][j]:
                            data_list[i][j] = None  # 若输入为空,则保证空值能输入至数据库
                    cursor.callproc('sp_updateData', data_list[i])

            if delete_id:
                delete_id_list = delete_id.split(',')
                for item_d in delete_id_list:
                    sql = 'delete from lesson where id = ' + str(item_d)
                    print sql
                    cursor.execute(sql)

            db.commit()
        except Exception as e:
            print str(e)
            return jsonify("保存至数据库失败: " + str(e))
    except Exception as e:
        return str(e)
        return jsonify("保存至数据库失败: " + str(e))
    finally:
        cursor.close()
        db.close()

    print data_list
    return jsonify("保存至数据库成功!")

if __name__ == '__main__':
    app.run()
