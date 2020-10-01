'''
라이브러리 dload 사용

이미지를 자동으로 다운로드 해주는 라이브러리 이며,
설치 방법은

"file-settings-project-python interpreter-(우측+버튼)-dload" 추가
'''

import dload
# 구글의 추석 이미지를 검색한 것을 받아와본다
dload.save("https://upload.wikimedia.org/wikipedia/commons/4/43/Korean_ancestor_veneration-Jesa-01.jpg")

