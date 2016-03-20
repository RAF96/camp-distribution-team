import xlrd
from student import Student

#name_file - файл для считывания списка участников лагеря .xls
def ReadXlsFile(name_input_file):
    rb = xlrd.open_workbook(name_input_file)
    result = list()
    for sheet in rb.sheets():
        list_of_students = list()
        for index in range(1, sheet.nrows):
            row = sheet.row_values(index)
            list_of_students.append(Student(row[1::]))
        result.append(list_of_students)
    return result
