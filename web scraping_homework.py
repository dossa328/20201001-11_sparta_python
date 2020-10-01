"""
웹 이미지 크롤링을 통해 좋아하는 연예인 사진을 가져와본다

** 나는 수지로 하겠음.
다음의 플로우를 따라감

1. 다음에서 수지 를 검색후 이미지 탭에서 아무 이미지를 선택한다
2. 이미지 오른쪽 클릭  -> 검사 -> 우측 개발자 탬에서 코드에 블록쳐진 부분에서 오른쪽 클릭 -> copy -> copy selector
3. 이미지에 대한 src를 불러 올 수 있게 된다
-> ' #imgList > div:nth-child(1) > a > img '

4. beautiful soup4와 webdriver를 import 해준다
5. 크롤러의 시간 제약을 주기 위해 time 도 호출
6. 받은 이미지 링크의 저장을 하기위한 패키지 dload 또한 import 해준다
"""


from bs4 import BeautifulSoup
# BeautifulSoup import
from selenium import webdriver
# webdriver import
import time
# time import
import dload
# dload import

# 다음은 chrome driver를 사용하기 위해 selenum을 호출
driver = webdriver.Chrome('chromedriver')
# 해당 경로는 본 py 파일과 같은 디렉토리에 위치한다
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EC%88%98%EC%A7%80")
# 이미지를 받아올 기본적인 웹 주소를 올려준다. 위의 주소는 다음 이미지 검색에서 "수지" 를 검색한 url 이다.

time.sleep(5)
# 웹이 뜨기위해 잠시동안  (5초) 간 기다린다.

req = driver.page_source
# 페이지에서 받아온 모든 데이터를 req에 저장함
soup = BeautifulSoup(req, 'html.parser')
# 받아온 html 정보를 soup에 저장인데 이부분에 대해 잘 이해가 안감.
# html.parser 가 의미하는 바를 잘 모르겠음

thumbnails = soup.select('#imgList > div > a > img')
# 검색된 이미지 중 하나에 대해 위 2번(주석)에 따라 진행된결과를 select로 호출
# 여기서 select는 조건에 맞는 모든 데이터를 가져온다
# 하나만 가져올 경우 select_one으로 호출할 수 있다.

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    # 썸네일에서 받아올 데이터는 'src' 이하 데이터만 필요함을 의미함.
    dload.save(img, f'imgs_homework/{i}.jpg')
    i += 1
# 다운로드 되는 파일 마다 같은 이름으로 저장할 수는 없으므로 위와 같이 f~{변수} 형태로 작성하며, i는 이미지가 다운될때마다 1씩 증가한다


driver.quit() # 끝나면 닫아주기

# 다 사용된 드라이버는 종료 시켜주는것으로 보임.