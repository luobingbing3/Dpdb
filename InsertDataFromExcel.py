# -*- coding: utf-8 -*-
import pandas as pd
from datetime import date
import MySQLdb
from math import isnan


# 该函数用于课程数据,从excel表格插入数据库的lesson表格
# 输入参数: excel路径,数据库连接参数:host,user,passwd,db
# 返回参数: 若导入成功,则返回1, 若导入失败,则返回一个异常列表
def insertDataFromExcel(name_excel, host_='localhost', user_='root', passwd_='1111', db_='Dpdb'):

    # 连接数据库
    try:
        conn = MySQLdb.connect(host=host_, user=user_, passwd=passwd_, db=db_, charset='utf8')
    except Exception, e:
        return [e]
    conn.autocommit(0)
    cursor = conn.cursor()

    try:
        excel_data = pd.read_excel(name_excel, header=0, skiprows=range(32,50), index_col=0)
    except Exception, e:
        return [e]

    error_list = []

    # 由于第一行被用作index, '学号'被提取成index,所以提取出来添加到内容当中
    student_id = pd.Series([excel_data.keys()[0]], index=[u'学号'])

    basic_data = excel_data.iloc[:6, 0]
    number_data = excel_data.T.count()[6]

    # 往student与coach表中写入数据
    stu_coach_info = pd.Series()
    stu_coach_info = stu_coach_info.append(student_id)
    stu_coach_info = stu_coach_info.append(basic_data[:6])

    try:
        cursor.callproc('sp_insertStuCoach', stu_coach_info)
    except Exception, e:
        error_list.append(e)
        pass

    for j in range(number_data):
        try:
            row = basic_data
            row = row.append(student_id)
            # 提取日期,判断,若年月日都有值且有效,则判断该条数据有效
            date_ = excel_data.iloc[6:9, j]
            # 检查日期输入格式
            try:
                date_st = date(int(date_[0]), int(date_[1]), int(date_[2]))
            except Exception, e_date:
                raise Exception('Date: ' + e_date.message)
            row = row.append(pd.Series([date_st], index=[u'日期']))
            # 检查课次输入格式
            try:
                if isnan(excel_data.iloc[9, j]):
                    raise Exception('Lesson number is missing.')
            except Exception, ee:
                raise Exception('Lesson number: ' + ee.message)
            # 将剩余信息输入
            row = row.append(excel_data.iloc[9:, j])
            # 将多余项删除
            row = row.drop([u'姓名', u'年龄（岁）', u'教练姓名', u'身高（cm）', u'性别'])
            # 检查重复行,若发现重复行(学员id,教练id,日期,课次均一致),则覆盖. 若非重复行,则插入
            cursor.callproc('sp_insertData', row)
        except Exception, e:
            error_list.append(Exception('Colume ' + '%d'%(j+1) +': ' + e.message))
            pass
    if len(error_list):
        cursor.close()
        conn.close()
        return error_list
    conn.commit()
    cursor.close()
    conn.close()
    return 1
