# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
# 실행파일생성
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

#디자인 파일을 미리 롣링
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼클래스 정의(QMainWindow로 변경)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt 데모")
    def firstClick(self):
        #주소
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)
        #검색이 용이한 객체
        soup = BeautifulSoup(response.text, "html.parser")
        #검색
        f = open("daangn.txt", "wt", encoding="utf-8")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            priceElem = post.find("div", attrs={"class":"card-price"})
            addrElem = post.find("div", attrs={"class":"card-region-name"})
            title = titleElem.text.strip().replace("\n", "")
            price = priceElem.text.strip().replace("\n", "")
            addr = addrElem.text.strip().replace("\n", "")
            print(f"{title}, {price}, {addr}")
            f.write(f"{title}, {price}, {addr}\n")
        f.close()
        self.label.setText("첫번째 버튼 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")                
    

#직접 이 모듈을 실행한것을 체크 코드: 진입점(Entry Point)
if __name__ == "__main__":
    #실행 프로세스 생성
    app = QApplication(sys.argv)
    #폼 실행
    demoForm = DemoForm()
    #화면 보여주기
    demoForm.show()
    app.exec_()