#Demofile.py
#블럭을 선택하고 주석처리:ctrl + /_드러그해서 선택 후 ctrl + /_주석처리 해제:ctrl + /_드러그해서 선택 후 ctrl + /
# #파일쓰기
# f = open("c:\\work\\text.txt", "wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

# #파일읽기(raw string notation 사용)
# f = open(r"c:\\work\\text.txt", "rt", encoding="utf-8")
# print(f.read())  # 전체 내용 읽기
# f.close()
\


# 정규표현식
import re

result = re.search("[0-9]*th", "35th")
print(result) 
print(result.group())  # 검색된 문자열 출력

# 해당 블럭 선택후 ctrl + /_주석처리


# result = re.match("[0-9]*th", "35th")
# print(result)
# print(result.group())

# 파일쓰기
result = re.search("apple", "this is apple")
print(result.group())  

result = re.search(r"\d{4}", "올해는 2025년입니다.")
print(result.group()) 

result = re.search(r"\d{5}", "우리 동네는 51200입니다.")
print(result.group()) 
