# Demofile.py

# 파일 쓰기
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번쨰\n두번째\n세번째\n")
f.close()

#파일 읽기
f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)

# 다시 처음으로 파일 포인터 이동
f.seek(0)

# 한번에 한줄을 읽어서 처리
print(f.readline(), end="")
print(f.readline(), end="")

#전체를 리스트로 리턴
f.seek(0)
lst = f.readlines()
print(lst)

f.close()