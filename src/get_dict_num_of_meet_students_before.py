from os import listdir
from read_xls_file import ReadXlsFile

#AddOldSchool изменяет dict pairname_nummeet!
def AddOldSchool(pairname_nummeet):
    path = '../dat/DatOldCamp'
    files = listdir(path)
    counter = 0
    for name_file in files:
        a = ReadXlsFile(path +'/' + name_file)
        for sheet in a:
            for first in sheet:
                for second in sheet:
                    if first.name() + second.name() in pairname_nummeet:
                        pairname_nummeet[first.name() + second.name()] += 1
                        counter += 1
    print('Количество раннее встречавшихся пар', counter)

def GetDictPairName(list_of_students):
    pairname_nummeet = dict()
    for first in list_of_students:
        for second in list_of_students:
            if first.name() != second.name():
                pairname_nummeet[first.name() + second.name()] = 0
    return pairname_nummeet

def GetDictNumOfMeetStudentsBefore(list_of_students):
    pairname_nummeet = GetDictPairName(list_of_students)
    AddOldSchool(pairname_nummeet)
    return pairname_nummeet
