 *最底下可以对话哈哈哈！*


# Project Name: *Dpdb*

This is a small management system for dig-potency studio. We use [Flask](http://flask.pocoo.org/) which is a popular webdevelopment framework for Python. And this is the first project from Luo & Lyu.

Also, this is a gift for my friend Arrow. Hope this can make sense.

## Platform
1. Mac 10.11
2. Python 2.11
3. Flask 0.11
4. Mysql 5.7
5. jqGrid 5.1.1

## Installation
1. virtualenv, flask [Details](http://docs.jinkan.org/docs/flask/installation.html#virtualenv)<br>
	`sudo pip install virtualenv`<br>
	`mkdir myproject && cd myproject`<br>
	`virtualenv venv` <br>
	`sudo pip install flask`	
	

2. flask-mysql, pandas, pygal, xlrd <br>
	`sudo pip install flask-mysql` <br>
    `sudo pip install pandas` <br>
    `sudo pip install pygal` <br>
    `sudo pip install xlrd`

	
3. pycharm [Download](https://www.jetbrains.com/pycharm/download/) <br>
	`from flaskext.mysql import MySQL` 时会有`unresolved reference`的**错误**。按以下步骤解决。
	- `command + ,` -> `Project Interpreter` <br>
	![pycharm-conf-1](./conf-pic/pycharm-conf-1.png)
	
	- 进入`Add local` 选择 `venv/bin/pyhon` <br>
	![pycharm-conf-2](./conf-pic/pycharm-conf-2.png)
	
	- 此时，可以在package里看到已安装的package <br>
	![pycharm-conf-3](./conf-pic/pycharm-conf-3.png)
	
	- 点击确认之后，可以看到 `import Mysql` 已成功。

4. mysql 与 MYSQLWorkbench [Download](http://dev.mysql.com/downloads/mysql/)
	- 进入Mysql Workbench.
	- File -> Open SQL Script -> Find ./database_design/rou.sql -> Excute 
	- Find ./database_design/sp_insertData.sql -> Excute
	- Find ./database_design/sp_insertStuCoach.sql -> Excute
	- Find ./database_design/sp_updateData.sql -> Excute

5. jqGrid配置
	- 去[jqgrid官网](http://www.trirand.com/blog/?page_id=6)下载插件，解压。
	- 将解压后中的`jquery.jqGrid.min.js`与`grid.locale-cn.js`加入`static/js`文件夹中，将`ui.jqgrid.css`加入`static/css`中，前两个提供插件的功能支持，第二个是包括了语言转换支持，css文件为插件的外观支持。
	- jqgrid支持自定义主题外观，可到[网站](http://jqueryui.com/download/all/)下载外观主题，下载`jquery-ui-1.12.0.custom`外观，将文件夹改名为`jquery-ui`复制进`static`文件夹中。
	- 在`upload_homepage.html`中加入以下代码，将上述js与css文件加入:
<pre>`	<script src="../static/js/jquery-3.1.0.js"></script>
    <script src="../static/js/showAndDelete.js"></script>
     <script src="../static/js/grid.locale-cn.js" type="text/javascript"></script>
    <script src="../static/js/jquery.jqGrid.min.js" type="text/javascript"></script>
     <script src="../static/jquery-ui/jquery-ui.min.js" type="text/javascript"></script>
    <link href="../static/jquery-ui/jquery-ui.min.css" type="text/css" media="screen"
        rel="stylesheet">
     <link href="../static/css/ui.jqgrid.css" type="text/css" media="screen"
        rel="stylesheet">` </pre>
至此，配置基本结束。


## Database design (draft)

![table_design](./database_design/tables.png)

## Attention
1. Dpdb.py 中Mysql配置时的数据库名称、用户名要匹配。

## From Luo
### connect database
- 为了防止插入数据库汉字出现乱码:
	1. connect中设置charset='utf8'
	2. 保证数据库和表的编码都是utf8
	3. 保证pythonFile采用utf8编码

1. 创建好数据库之后，在Mysql workbench中运行’sp_insertStuCoach.sql‘，’sp_inserData.sql‘两个脚本，将两个过程存储入数据库当中；
2. 在点击进入上传界面时，点击‘选择文件’按钮，弹出对话框，选择excel(.xls, .xlsx)文件，可多选。点击‘上传’按钮，会弹出上传结果。若失败，则会输出错误信息；若上传成功，则会显示已上传的文件名，点击‘返回’可以返回至上一层。


3. 采用pandas的dataframe对excel表格完整拉取，为了防止出现意外，在date三行进行全值判断，有空，则判断该行无效；



## From Lyu
This is from Lyu, my job is to get data from database and analysis the data and draw some graphs and export some data for user to ananlysis.

Some details to be continue...


> Lyu @ Luo:
	我们把自己的东西往里加吧？以这个为模板。感觉如何？<br>
	2016.08.20

> Lyu @ Luo: 
    外面分别去完成homepagei.html 与 showResult.html<br>
	2016.08.22
	
> Lyu @ Luo: 
    我已经把画图和下拉基本功能实现了. <br>
    2016.08.26




