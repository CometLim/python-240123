# DemoRandomOS.py
# 사용 모둘 선언

import random
from os.path import *
import glob
from os import *

print(random.random())
print(random.random())

#리스트 내장
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

#유니크 샘플 생성
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))


lotto = list(range(1,45))
random.shuffle(lotto)
print(lotto)

print("--- 파일 다루기 ---")
print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))

fName = "c:\\python310\\python.exe"

if exists(fName):
    print("파일의 크기:{0}".format(getsize(fName)))
else:
    print("파일이 없음")

print("운영체제이름:", name)
print("환경변수:", environ)
# system("notepad.exe")

print(glob.glob("c:\\work\\*.py"))


