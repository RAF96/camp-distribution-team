from student import Student
from os import system
from xlrd import open_workbook
from xlwt import Workbook
from xlwt import easyxf
import xlwt

def GetValueTeam(team, dict_old_school):
    result = 0
    for first in team.students:
        for second in team.students:
            if first.name() + second.name() in dict_old_school:
                result += dict_old_school[first.name() + second.name()] ** 2
    return result

def WriteTeamInXls(team, path):
#system("cp ../dat/template.xls " + path)
    rb = open_workbook("../dat/template.xls", on_demand=True, formatting_info=True)
    rs = rb.sheet_by_index(0)
    wb = Workbook();
    ws = wb.add_sheet("1")
# Устанавливаем перенос по словам, выравнивание
    alignment = xlwt.Alignment()
    alignment.wrap = 1
    alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
# Устанавливаем шрифт
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.height = 12 * 20

# Создаём стиль с нашими установками
    style = xlwt.XFStyle()
    style.font = font
    style.alignment = alignment
    e = 10000 // 3 
    size_col = [e, 2 * e, 2 * e, 2 * e, 3 * e, e, e]
    size_row = e // 5 
    first_row = rs.row_values(0)
    for index in range(len(first_row)):
        ws.col(index).width = size_col[index]
        ws.write(0, index, first_row[index], style)
    ws.row(0).height = size_row
    for index_student in range(0, len(team)):
        student = team.students[index_student]
        row = index_student + 1
        ws.row(row).height = size_row 
        ws.write(row, 0, row, style)
        for index_option in range(0, len(student)):
            column = index_option + 1
            option = student[index_option]
            ws.write(row, column, option, style)
    wb.save(path)

class Team(object):
    
    def __init__(self):
        self.students = list()

    def append(self, schoolboy):
        self.students.append(schoolboy)

    def sort(self):
        self.students.sort()

    def __repr__(self):
        return ''.join([str(e) + '\n' for e in self.students])

    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        return self.students[index]

    def __setitem__(self, index, value):
        self.students[index] = value
