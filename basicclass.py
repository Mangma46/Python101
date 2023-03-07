class School:
    #Attribute
    SchoolName = 'KMUTT'

    #Constructoe
    def __init__(self,subject='Python Programing'):
        print('Show text if have create instance')
        self.subject=subject

    #Method
    def hello(self):
        print('Good Morning every body')
    
    def teach(self):
        print(f'This school teach {self.subject}')

#Instance
#school1 = School('Physics')
#print(f'School name are: {school1.SchoolName}')
#school1.hello()
#school1.teach()

class Student(School):
    def __init__(self,fullname,level,scores,subject):
        super().__init__(subject)
        self.fullname=fullname
        self.level=level
        self.scores = scores

    def checkGrade(self):
        if self.scores >= 80:
            print(f'{self.subject}: A')
        elif self.scores >= 70:
            print(f'{self.subject}: B')
        elif self.scores >= 60:
            print(f'{self.subject}: C')
        elif self.scores >= 50:
            print(f'{self.subject}: D')
        else :
            print(f'{self.subject}: F')

Student01=Student('Akkarachai',12,75,'Math')
print(f'SchoolName: {Student01.SchoolName}')
print(f'Level: {Student01.level}')
print(f'Scores: {Student01.scores}')
Student01.checkGrade()

Student02=Student('Paully',12,95,'Cal')
print(f'SchoolName: {Student02.SchoolName}')
print(f'Level: {Student02.level}')
print(f'Scores: {Student02.scores}')
Student02.checkGrade()
    




