# requests 모듈 => 웹페이지를 요청하고 응답 데이터를 받을 수 있음
import requests as req
from bs4 import BeautifulSoup # html 해석도구

print(f'\nrequests: \n{req}')

response = req.get('https://news.naver.com/')
print(f'\nresponse: \n{response}')
#print(f'\ntext: \n{response.text}')

soup = BeautifulSoup(response.text, 'html.parser')

content = soup.select('.cnf_news_item')
print(content[0].text)

print('== class로 선택, 반복문으로 텍스트 출력')
for c in content:
    print(c.text)
