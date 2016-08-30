# -*- coding: utf-8 -*-
import pygal
from datetime import date

def graph_line_init():
    graph = []
    graph_title = [u"体重表", u"体脂含量表", u"胸围(最高处)表", u"腰围(最高处)表", u"臀围表", u"臀腰比表", u"大腿围表"]

    graph_y_title = [u"kg", u"%", u"cm", u"cm", u"cm", u"", u"cm"]
    for i in range(7):
        graph_line = pygal.Line(title=graph_title[i])
        graph_line.x_title = u'课次'
        graph_line.y_title = graph_y_title[i]
        graph_line.x_labels = map(str, range(1, 11))
        graph.append(graph_line)
    return graph

def init():
    """ show the init graphs which are no-data graphs."""
    graph_line = graph_line_init()
    graph_info = []
    for gl in graph_line:
        gi = gl.render_data_uri()
        graph_info.append(gi)
    return graph_info

def draw(cursor, stu_id, stu_text, opt):
    """ accoding to the selected option in student_select, draw the student's 7 indexes."""
    graph_info = []
    sql = "select weight, body_fat, chest_circumference_max, waistline_navel, hipline, WHR, thigh_circumference, " + opt + " from lesson where student_id = " + str(stu_id)
    print sql
    cursor.execute(sql)
    results = cursor.fetchall()

    graph_title = [u"体重表", u"体脂含量表", u"胸围(最高处)表", u"腰围(最高处)表", u"臀围表", u"臀腰比表", u"大腿围表"]
    graph_y_title = [u"kg", u"%", u"cm", u"cm", u"cm", u"", u"cm"]

    if opt == "number_":
        for i in range(7):
            graph_line = pygal.XY(title=graph_title[i])
            graph_line.x_title = u'课次'
            graph_line.y_title = graph_y_title[i]
            # graph_line.x_labels = (1,2,3,4,5,6,7,8,9,10)
            data_line = []
            for row in results:
                data_line.append((row[7], row[i]))
            graph_line.add(stu_text, data_line)
            gi = graph_line.render_data_uri()
            graph_info.append(gi)
    else :
        for i in range(7):
            graph_line = pygal.DateLine(x_label_rotation=25)
            graph_line.x_value_formatter=lambda dt:dt.strftime('%y.%m.%d')
            graph_line.x_title = u'日期'
            graph_line.y_title = graph_y_title[i]
            data_line = []
            for row in results:
                data_line.append((row[7], row[i]))
            graph_line.add(stu_text, data_line)
            gi = graph_line.render_data_uri()
            graph_info.append(gi)

    return graph_info
