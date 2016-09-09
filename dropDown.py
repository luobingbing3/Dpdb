# -*- coding: utf-8 -*-


def init(cursor):
    """get the default dropdown-select option results(id & name_) from mysql when open the whoResult.html"""
    coach_info = []
    student_info = []
    sql1 = "select id, name_ from coach"
    sql2 = "select id, name_ from student"
    cursor.execute(sql1)
    results = cursor.fetchall()
    for row in results:
        coach_info.append((row[0], row[1]))
    cursor.execute(sql2)
    results = cursor.fetchall()
    for row in results:
        student_info.append((row[0], row[1]))
    return coach_info, student_info


def filter( cursor, current_coach):
    """get the selected dropdown option results(id & name_) from mysql after new choice made."""
    student_list = []
    sql = "select id, name_ from student "
    if current_coach != 0:
        sql += "where coach_id = " + str(current_coach)
        print sql
    else :
        print sql
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        student_list.append((row[0], row[1]))
    print "filterStudent success!"
    return student_list
