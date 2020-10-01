'''
이미지 웹 스크래핑(크롤링 하기)

이번 차시에서는 파이썬으로 브라우저 제어할것임
본 과정에선 두가지 패키지가 필요하다
1. selenum 패키지를 이용
-> chrome web driver를 동일 디렉토리에 추가함
(자동화)

2. beautifulsoup 사용
-> 프루닝작업에 이용
(솎아내기)
'''

# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver')
#
# driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0 ")


from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload
# 파이썬 내장함수

driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
# 웹 띄우기
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################

# thumbnails = soup.select_one('#imgList > div:nth-child(2) > a > img')
# thumbnails = soup.select_one('#imgList > div:nth-child(2) > a > img')['src']

thumbnails = soup.select('#imgList > div > a > img')
# select -> 조건에 맞는 이미지 전부 불러오기
# 이미지를 보니 :nth-child(12) 부분만 빼고 다 같더라. 그래서 삭제
# -> #imgList > div > a > img

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'img/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫아주기
