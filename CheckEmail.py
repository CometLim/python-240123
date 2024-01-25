# CheckEmail.py
import re

def check_email(email):
    # 이메일 주소 정규식 패턴 
    # raw string notation: 날것 그대로 표기
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # re.search() 함수를 사용하여 패턴 검사
    match = re.search(pattern, email)
    
    if match:
        print(f"{email}은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일 주소입니다.")

# 샘플 이메일 주소 10개
sample_emails = [
    'user@example.com',
    'john.doe123@gmail.com',
    'info@company.co.kr',
    'invalid-email',
    'another_user@domain',
    'test.email@subdomain.domain.com',
    'user@localhost',
    'no_at_sign.com',
    'user@.dot_at_start.com',
    '@dot_at_start.com',
    'user@dot_at_end.',
]

# 각각의 샘플 이메일에 대해 체크 수행
for email in sample_emails:
    check_email(email)
