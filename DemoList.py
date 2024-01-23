# DemoList.py

strA = "Python is very powerful"
print(strA)
print(strA[0:6])
print(strA[-3:])

# 바로 실행 : ctrl + F5
colors = ["red", "blue", "green"]
print(len(colors))
colors.append("white")
print(colors)
colors.insert(1, "black")
print(colors)

colors += ["red"]
colors += "red"
print(colors)
print(colors.count("red)"))
print(colors.index("blue"))
colors.remove("red")
print(colors)

print("---set---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---tuple---")
tp = (1,2,3)
print(len(tp))

#함수를 정의
def calc(a,b):
    return a+b, a*b

#함수를 호출
result = calc(3,4)
print(result)
print(result[0])
print(result[1])

print("id:%s, name:%s" % ("kim", "김유신"))

args = (5,6)
print(calc(*args))

print("---형식변환---")
a = list({1,2,3})
print(a)
print(type(a))
a.append(4)
print(a)

