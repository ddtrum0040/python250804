#db1.py
import sqlite3

#연결객체를 리턴(메모리 임시
#파일에 저장
con = sqlite3.connect(r"c:\work\smaple.db")  # 파일 DB 사용
#커서객체 리턴
cur = con.cursor()

#con = sqlite3.connect(":memory:")  # 메모리 DB 사용
#커서객체를 리턴
#cur = con.cursor()
#테이블 생성
cur.execute("create table PhoneBook (name text, phone text);")
#데이터 삽입
cur.execute("insert into PhoneBook values ('홍길동', '010-1234-5678');")

#입력 파라메터 처리
name = '이순신'
phone = '010-9876-5432'
cur.execute("insert into PhoneBook values (?, ?);", (name, phone))

#여러건 입력
datalist = (("김길동","010-111"),("전우치","010-222"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)


#데이터 조회
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)  # ('홍길동', '010-1234-5678')

#작업을 정상적 종료
con.commit()
