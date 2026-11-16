# 브라우저를 실행하고 조작하는 객체
from selenium import webdriver 
# 요소를 찾을 때 사용하는 선택 방식 지정 도구
from selenium.webdriver.common.by import By

# 1) 브라우저 실행
driver = webdriver.Chrome()

# 2) 웹페이지 접속 
# get(): 특정 웹페이지로 이동하는 명령어
driver.get("https://quotes.toscrape.com/")

# 3) 요소 하나 찾기
quote = driver.find_element(By.CLASS_NAME, "text")
quotes = driver.find_elements(By.CLASS_NAME, "text")

# 4) 텍스트 가져오기
#print(f'\nquote: \n{quote.text}')
seq = 1
for q in quotes:
    #print(f'\nquotes{seq}: \n{q}')
    seq += 1

# -------------------------------------------------

# 태그로 요소 찾기
div_elements = driver.find_elements(By.TAG_NAME, 'div')
print(f'\nDiv 태그 개수: {len(div_elements)}')

# 클래스로 요소 찾기
class_elements = driver.find_elements(By.CLASS_NAME, 'text')
print(f'\ntext Class 개수: {len(div_elements)}')

# xPath로 찾기
#   xPath: HTML의 구조(경로)를 이용해 요소 찾는 방법
#   id나 class로 찾기 어려울 때 사용
#   HTML 트리구조를 따라가면서 원하는 요소를 지정할 수 있음
# 장점
#   조건이나 경로로 정화하게 요소 선택 가능
# 단점
#   페이지 구조가 바뀌면 xPath도 같이 깨질 수 있음

# XPath로 첫 번째 명언 검색
xpath_quote_text = driver.find_element(
    By.XPATH,
    "//div[@class='quote']/span[@class='text']"
)
print(f'\nxPath로 찾은 첫 번째 명언 : \n{xpath_quote_text.text}')

# XPath의 위치 인덱스는 1부터 시작
xpath_first_block = driver.find_element(
    By.XPATH,
    "(//div[@class='quote'])[1]"
)

# 첫 번째 블록 내부에서 작성자 검색
xpath_first_author = xpath_first_block.find_element(
    By.CLASS_NAME,
    'author'
)
print(f'\nxPath로 찾은 첫 번째 저자 : {xpath_first_author.text}')


#input("\n종료하려면 Enter를 누르세요...")
driver.quit()
