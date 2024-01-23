#전역변수
strName = "Not Class Member"

#클래스 정의
class GString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(self.strName)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
