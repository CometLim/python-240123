# func2.py
# 가변인자를 처리하는 함수

def union(*ar): # * 하나 튜플
    #지역변수
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 함수를 호출(중단점 - Break Point 14에 설정)
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

#필수 입력과 옵션 입력이 있는 경우
#딕셔너리 형태를 사용
def userURIBuilder(server, port, **user): # **이면 딕셔너리
    strURL = "https://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL
#호출
print (userURIBuilder("mycampus.com", "443", id="lim", name="hyeonjin"))
print (userURIBuilder("mycampus.com", "443", id="lim", name="hyeonjin", age="31"))

# 람다함수

g = (lambda x,y:x*y)
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())


print("--- 필터링 하는 함수 ---")
def getBiggerthan20(i):
    return i>20

lst = [10, 25, 30]
# 파이썬음 참조가 전달된다(Pass By Reference)
itemL = filter(getBiggerthan20, lst)  
for i in itemL:
    print(i)

print("--- 람다함수 ---")
itemL = filter(lambda x:x>20, lst)
for i in itemL:
    print(i)