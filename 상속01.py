#부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스
class Student(Person):
    #덮어쓰기(Overriding)
    def __init__(self, name, phoneNumber, subject, studentID):
        #sself.name = name
        #self.phoneNumber = phoneNumber
        #부모의초기화 메서드 호출 
        super().__init__(name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기(Overriding)
    def printInfo(self):
        print("Info(이름:{0}, 전화번호: {1})".format(
            self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(
            self.subject, self.studentID))
        

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
#print(p.__dict__)
#print(s.__dict__)
p.printInfo()
s.printInfo()



