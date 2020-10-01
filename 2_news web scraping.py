from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')


articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')


# 기사 전문을 가지고 온다
# print(articles)
# # 텍스트만 가지고 온다
# print(articles.text)

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

for article in articles:
    title = article.select_one('dl > dt > a').text
    # print(title.text) <- 이렇게 써도됨
    url = article.select_one('dl > dt > a')['href']

    company = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사','')
    # 신문사명 -> # sp_nws1 > dl > dd.txt_inline > span._sp_each_source

    ws1.append([title, url, company])
    print(title, url, company)

driver.quit()
wb.save(filename="articles.xlsx")
