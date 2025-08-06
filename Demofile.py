#Demofile.py

#파일쓰기
f = open("c:\\work\\text.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일읽기(raw string notation 사용)
f = open(r"c:\\work\\text.txt", "rt", encoding="utf-8")
print(f.read())  # 전체 내용 읽기
f.close()


