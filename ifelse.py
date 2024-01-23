# ifelse.py

# score = int(input("점수를 입력\n점수 : "))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 80 <= score < 90:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade, "입니다.")

print("--- 반복 구문 ---")
vaule = 5
while vaule > 0 :
    print(vaule)
    vaule -= 1

print("--- for in ----")
lst = ["문자열", 100, 3.14]
for item in lst:
    print(item, type(item))

# lst = list(range(1,11))
# print(lst)
# for item in lst:
#     print("Item:{0}".format(item))

print("--- break ---")
lst = list(range(1,11))
print(lst)
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))

print("--- continue ---")
lst = list(range(1,11))
print(lst)
for item in lst:
    if item % 2 == 0:
        continue
    print("Item:{0}".format(item))

print("--- 리스트 내장---")
lst  = list(range(1,11))
print([i**2 for i in lst if i> 5])
tp = ("apple", "orange", "kiwi")
print([len(i) for i in tp])