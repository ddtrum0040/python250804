#개발자 클래스를 정의
class Developer:
    def __init__(self, name, phoneNumber, language):
        self.name = name
        self.phoneNumber = phoneNumber
        self.language = language

    def printInfo(self):
        print("Info(이름:{0}, 전화번호: {1}, 언어: {2})".format(
            self.name, self.phoneNumber, self.language))
        
#인스턴스를 2개 생성
d1 = Developer("홍길동", "010-1234-5678", "Python")
d2 = Developer("김철수", "010-8765-4321", "Java") 

#정보 출력
d1.printInfo()
d2.printInfo()