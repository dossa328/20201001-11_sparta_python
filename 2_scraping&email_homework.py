import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver


def sendmail(me, emails):
    for target in emails:
        # 메일 기본 정보 설정
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "[공유] 추석기사"
        msg['From'] = me
        msg['To'] = target

        # 메일 내용 쓰기
        content = "추석때 뭐하고있니!"
        part2 = MIMEText(content, 'plain')
        msg.attach(part2)

        # 파일 첨부하기###############
        part = MIMEBase('application', "octet-stream")
        with open("daily_news.xlsx", 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
        msg.attach(part)
        ###################################

        # 메일 보내고 서버 끄기
        s.sendmail(me, target, msg.as_string())

    s.quit()


def scrapnews_excel_thumnail(url_in):
    driver = webdriver.Chrome('chromedriver')

    url = url_in

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
    ws1.title = "daily_news"
    ws1.append(["제목", "링크", "신문사", "썸네일"])

    for article in articles:
        title = article.select_one('dl > dt > a').text
        thumnail = article.select_one('div > a > img')['src']
        # print(title.text) <- 이렇게 써도됨
        url = article.select_one('dl > dt > a')['href']

        company = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사','')
        # 신문사명 -> # sp_nws1 > dl > dd.txt_inline > span._sp_each_source

        ws1.append([title, url, company, thumnail])
        # print(title, url, company)

    driver.quit()
    wb.save(filename="daily_news.xlsx")


# mail initialization
# 보내는 사람 정보
me = "dossa328@gmail.com"
my_password = "hayate13579@"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
# target = "dossa328@naver.com"

# 다중 발송
emails = ['dossa328@naver.com']

sendmail(me, emails)

#####################################
# scraping news & makes excel file

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"
scrapnews_excel_thumnail(url)
