# -*- coding: utf-8 -*-


def selectItemsFromLesson(cursor, coach_id, student_id):
    sql = 'select * from lesson '
    if coach_id != 0 and student_id != 0:
        sql += 'where coach_id = ' + str(coach_id) + ' and student_id = ' + str(student_id)
        print sql
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# def updateData(updatedata):
