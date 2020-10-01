# 쓰기
# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕, 스파르타!\n")
#
# for i in [1,2,3,4,5]:
#     f.write(f"{i}번째 줄입니다\n")
#
# f.close()

# 읽기
# text = ' '
#
# with open("kakaotalk2.txt", "r", encoding="utf-8") as f:
#     # 한줄씩 파일 읽기
#     lines = f.readlines()
#     for line in lines:
#         text += line
#
# print(text)

# font 탐색
# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)
#
#
# # C:\Users\JungHyunDo\AppData\Local\Microsoft\Windows\Fonts\NanumBarunGothicBold.ttf

from PIL import Image
import numpy as np
from wordcloud import WordCloud

text = ''
i=1
remov = ['그럼', '진짜','샵검색','나도','이제','근데','아니','다들','내가','오늘','그냥','지금','그거','그래서','누나', '나는',
         '언니', '이거', '너무', '저거', '마자', '우리','허허','ㄷㄷ','심각','일단','어제','제가','ㅎㅎ','누가','아직','뭐야',
         '내일','마지막','활동기록','원래','ㅋ','사진','이모티콘\n','삭제된','메시지입니다','ㅠ','ㅜ','ㅇ','ㄱ','저는','저도','요즘',
         '그래','그치','아냐','역시','맞아']
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    # 한줄씩 파일 읽기
    lines = f.readlines()
    for line in lines[5:]:
        print("{}%".format(i/len(lines)*100))
        if '] [' in line:
            line = line.split('] ')[2]
            for rv in remov:
                line = line.replace(rv, '')
            text += line
        i += 1

font_path = "C:/Users/JungHyunDo/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothicBold.ttf"
# print(text)

wc = WordCloud(font_path=font_path, background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result_lu.png")

# 이미지 지정
# mask = np.array(Image.open('think_cloud.png'))
# wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
# wc.generate(text)
# wc.to_file("hs_kakao.png")