#코파일럿_코스피200정보.py

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://finance.naver.com/sise/sise_index.naver?code=KPI200"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# '편입종목상위' 테이블(class='type_1')에서 데이터 추출
items = []
table = soup.find("table", class_="type_1")
if table:
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) == 7:
            name = cols[0].get_text(strip=True)
            price = cols[1].get_text(strip=True)
            change = cols[2].get_text(strip=True)
            rate = cols[3].get_text(strip=True)
            volume = cols[4].get_text(strip=True)
            amount = cols[5].get_text(strip=True)
            marketcap = cols[6].get_text(strip=True)
            items.append([name, price, change, rate, volume, amount, marketcap])

# 엑셀 저장
wb = Workbook()
ws = wb.active
ws.title = "KOSPI200"
ws.append(["종목명", "현재가", "전일비", "등락률", "거래량", "거래대금(백만)", "시가총액(억)"])
for item in items:
    ws.append(item)

wb.save("KOSPI200Result.xlsx")

print("코스피200 편입종목 상위 리스트:")
for item in items:
    print(item)
