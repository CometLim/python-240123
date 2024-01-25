#주민등록번호 체크
import re

def check_jumin(jumin):
    # 주민등록번호 정규식 패턴
    pattern = r'^(\d{6})[-](\d{7})$'
    
    # re.search() 함수를 사용하여 패턴 검사
    match = re.search(pattern, jumin)
    
    if match:
        print(f"{jumin}은(는) 유효한 주민등록번호입니다.")
        birth_date, unique_number = match.groups()
        print(f"생년월일: {birth_date}, 고유번호: {unique_number}")
    else:
        print(f"{jumin}은(는) 유효하지 않은 주민등록번호입니다.")

# 사용자로부터 주민등록번호 입력 받기
num_of_samples = 10
sample_jumins = []
for i in range(num_of_samples):
    jumin = input(f"주민등록번호 예시 {i+1}/{num_of_samples}: ")
    sample_jumins.append(jumin)

# 각각의 사용자 입력 주민등록번호에 대해 체크 수행
for jumin in sample_jumins:
    check_jumin(jumin)
