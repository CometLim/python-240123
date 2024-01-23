# function1.py
#1) 함수를 정의
def setValue(newValue):
    #지역변수에 초기화
    x = newValue
    print("함수내부:", x)

#2) 함수를 호출
retValue = setValue(5)
print(retValue)

#함수정의
def swap(x,y):
    return y,x

#호출
retValue = swap(3,4)
print(retValue)


#전역변수와 지역변수 호출
x = 5
def func1(a):
    return a+x

#호출

print(func1(1))

def func2(a):
    #지역변수
    x = 10
    return a+x

#호출
print(func2(1))

#기본값이 있는 함수 정의
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5, 6))

#키워드 인자 방식(매개변수명 상세하게 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURI("naver.com", "80"))
print(connectURI(port="9090", server="nhvc.nhbank.com"))