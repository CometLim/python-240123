#DemoRE.py

import re

#전체를 검새
result = re.search("[0-9]*th", " 35th")
print(result)
print(result.group())

#정확하게 일치
# result = re.match("[0-9]*th", "35th")
# print(result)
# print(result.group())

result = re.search("\d{4}","올해는 2024년 입니다.")
print(result.group())

result = re.search("\d{5}","우리 동네는 52100입니다.")
print(result.group())

result = re.search("apple","this sis apple")
print(result.group())