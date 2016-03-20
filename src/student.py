

class Student(object):
    def __init__(self, option):
        self.option = option
    
    def name(self):
        return self.option[0]
    
    def __lt__(self, other):
        return self.option < other.option

    def __repr__(self):
        return self.option[0]

    def __str__(self):
        return self.option[0]
    
    def __getitem__(self, index):
        return self.option[index] 
    
    def __len__(self):
        return len(self.option)
