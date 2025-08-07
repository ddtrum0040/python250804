#web2.py


from bs4 import BeautifulSoup
import urllib.request
import re


#파일로 저장
f = open('clien.txt', 'wt', encoding='utf-8')
#페이징 처리(번호를 생성)
for i in range(1, 10): 
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)  # 페이지 번호를 URL에 추가(조작가능)
    #url = "https://www.clien.net/service/board/sold" #원래 URL    
    print(url)  # URL 확인용 출력
    #함수 체인(메서드 체인)
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    for tag in soup.find_all('span', attrs={'data-role':'list-title-text'}):
        title = tag.text.strip()  # 문자열 앞뒤 공백 제거
        if re.search('애플워치', title):
            print(title)
            f.write(title + '\n')  # 파일에 제목 저장
f.close()  # 파일 닫기



# 페이지 로딩
#<span class="subject_fixed" data-role="list-title-text" title="아이폰 13미니 256 팝니다">
#아이폰 13미니 256 팝니다
#</span>

