from camp import Camp
from camp import WriteCampInXls
from read_xls_file import ReadXlsFile 
from get_dict_num_of_meet_students_before import GetDictNumOfMeetStudentsBefore

def main():
    num_of_team = 5
    path_to_list_of_students = '../dat/Spisok_uchastnikov.xls'
    list_of_students = ReadXlsFile(path_to_list_of_students)
    c = Camp(num_of_team)
    c.MakeCamp(list_of_students[0], GetDictNumOfMeetStudentsBefore(list_of_students[0]))
    WriteCampInXls(c, path = '../res/')

if __name__ == '__main__':
    main()
