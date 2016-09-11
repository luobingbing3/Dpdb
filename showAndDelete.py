# -*- coding: utf-8 -*-


def selectItemsFromLesson(cursor, coach_id, student_id):
    sql = 'select * from lesson '
    if coach_id != 0 and student_id != 0:
        sql += 'where coach_id = ' + str(coach_id) + ' and student_id = ' + str(student_id)
        print sql
    if coach_id != 0 and student_id == 0:
        sql += 'where coach_id = ' + str(coach_id)
    if student_id == -1:
        return 0
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# def updateData(updatedata):
