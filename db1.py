# db1.py

import sqlite3

# 연결객체
con = sqlite3.connect("sample.db")

#커서객체
cur = con.cursor()

#테이블을 생성
cur.execute("create table if not exists PhoneBook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('신철호', '010-9936-1552');")
cur.execute("insert into PhoneBook values ('이진엽', '010-9500-1608');")
#입력 파라메터 처리
name = "김다예"
phoneNum = "010-5676-1412"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))
# 여러개 행을 입력
datalist = (("김충호", "010-2489-1958"), ("김재범", "010-9284-6828"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook order by name;")
for row in cur:
    print(row)
# print("---fecthone()---")
# print(cur.fetchone())
# print("---fecthone(2)---")
# print(cur.fetchmany(2))
# print("---fetchall()---")
# print(cur.fetchall())
# cur.execute("select * from PhoneBook;")
# print(cur.fetchall())
    
# 작업 정상적으로 완료
con.commit()