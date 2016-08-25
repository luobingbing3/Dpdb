# -*- coding: utf-8 -*-
from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from InsertDataFromExcel import insertDataFromExcel
import os

app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'      # 输入自己数据库的用户名
app.config['MYSQL_DATABASE_PASSWORD'] = '1111'  # 输入自己数据库用户名的密码
app.config['MYSQL_DATABASE_DB'] = 'Dpdb'  # 我们要使用的数据库名字
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # 要使用数据库的网址
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
def homepage():
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
    return render_template('showResult.html')


if __name__ == '__main__':
    app.run()
