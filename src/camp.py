from team import Team
from team import GetValueTeam
from team import WriteTeamInXls
from random import randint
from random import seed

def WriteCampInXls(camp, path):
    for index in range(camp.num_of_camp):
        WriteTeamInXls(camp.teams[index], path + str(index + 1) + '.xls')

class Camp(object):
   
    def __init__(self, num_of_camp):
        self.num_of_camp = num_of_camp
        self.teams = [Team() for i in range(num_of_camp)] 

    def MakeCamp(self, list_of_students, dict_old_school):
        self.MakeTestCamp(list_of_students)
        self.MinimizingNumOfMeet(dict_old_school)
        for element in self.teams:
            element.sort()
        
    def MakeTestCamp(self, list_of_students):
        for i in range(len(list_of_students)):
            self.teams[i % self.num_of_camp].append(list_of_students[i])

    def GetValueCamp(self, dict_old_school):
        return sum([GetValueTeam(self.teams[i], dict_old_school) \
            for i in range(self.num_of_camp)])

    def MinimizingNumOfMeet(self, dict_old_school):
        seed(4)
        result = self.GetValueCamp(dict_old_school)
        step = 0
        last_good_step = 0
        while step - last_good_step < 100:
            list_change = list()
            for i in range(randint(1, 5)):
                first_team = self.teams[randint(0, self.num_of_camp - 1)]
                second_team = self.teams[randint(0, self.num_of_camp - 1)]
                first_index = randint(0, len(first_team) - 1)
                second_index = randint(0, len(second_team) - 1)
                (first_team[first_index], second_team[second_index]) = \
                    (second_team[second_index], first_team[first_index]) 
                list_change.append((first_team, first_index, second_team, second_index))
                # WhatIsListChange
            list_change.reverse()
            result_after_change = self.GetValueCamp(dict_old_school)
            if result_after_change < result:
                result = result_after_change
                last_good_step = step
            else:
                for change in list_change:
                    first_team = change[0]  # Смотреть строку с комментарием WhatIsListChange
                    first_index = change[1]
                    second_team = change[2]
                    second_index = change[3]
                    (first_team[first_index], second_team[second_index]) = \
                        (second_team[second_index], first_team[first_index]) 
                # Тестирование, что возвращение прошло успешно
                result_test = self.GetValueCamp(dict_old_school)
                if result != result_test:
                    raise NameError('ValueCamp после обратных операций стал неверным')
            step += 1
