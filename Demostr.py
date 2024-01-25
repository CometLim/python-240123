# Demostr.py

# print ( dir(str) )

strA = "python is powerful"
strB= "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize)
print(strA.count("p"))
print(strA.count("p",7))
print("--- 시작 종료 패턴 ---")
print(strA.startswith("py"))
print(strA.endswith("ful"))

print("MBC2580".isalnum())
print("MBC : 2580".isalnum())
print("2580".isdecimal())

print("--- 반복 문구 ---")
names = ["홍길동", "이순신", "전우치"]
for name in names:
    print("안녕하세요 {0}님 추운 겨울입니다.".format(name))
    print("=" * 40)

print("--- 공백문자 제거 ---")
data = "<<< spam and ham >>>"
print(data)

#삭제할 문자 지정
result = data.strip("<> ")
print(result)

#변환
result2 = data.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print("--- 하나의 문자열로 합치기 ---")
print(":)".join(lst))