# DemoDict.py

device = {"아이폰": 5, "아이패드": 10, "윈도우타블렛": 15}

print(type(device))
print(len(device))

#입력
device["맥북"] = 15
print(device)

#디버깅
for item in device.items():
    print(item)

#수정
device["아이폰"] = 6

#삭제
del device["아이패드"]
print(device["아이폰"])
print(device)

#전화번호
phone = {"kim" : "111", "lee": "222", "park" : "333"}
for k,v in phone.items():
    print(k,v)

print("kim" in phone)
print("kang" not in phone)


#참조만 복사
p = phone
print(p)
p["kang"] = "1234"
print(phone)
print(p)
print(id(phone), id(p))