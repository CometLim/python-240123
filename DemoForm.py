# DemoForm.py
# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일을 미리 롣링
form_class = uic.loadUiType("DemoForm.ui")[0]

#폼클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt 데모")

#직접 이 모듈을 실행한것을 체크 코드: 진입점(Entry Point)
if __name__ == "__main__":
    #실행 프로세스 생성
    app = QApplication(sys.argv)
    #폼 실행
    demoForm = DemoForm()
    #화면 보여주기
    demoForm.show()
    app.exec_()