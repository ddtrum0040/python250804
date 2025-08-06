import re

def is_valid_email(email):
    # 이메일 주소가 맞는지 확인하는 규칙(정규표현식)입니다.
    # r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # 
    # ^ : 이메일의 시작을 의미해요.
    # [a-zA-Z0-9._%+-]+ : 
    #   영어 대소문자(a-zA-Z), 숫자(0-9), 점(.), 밑줄(_), 퍼센트(%), 더하기(+), 빼기(-)가 한 번 이상 나와야 해요.
    #   이 부분이 이메일의 앞부분(아이디)이에요.
    # @ : 꼭 @가 있어야 해요. 이메일은 항상 @가 들어가요.
    # [a-zA-Z0-9.-]+ : 
    #   영어 대소문자, 숫자, 점(.), 빼기(-)가 한 번 이상 나와야 해요.
    #   이 부분이 이메일의 뒷부분(도메인)이에요.
    # \. : 점(.)이 꼭 있어야 해요. 도메인과 마지막 부분을 나눠줘요.
    # [a-zA-Z]{2,} : 
    #   영어 대소문자가 2글자 이상 나와야 해요. (예: com, net, kr)
    # $ : 이메일의 끝을 의미해요.
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 테스트용 이메일 주소 10개
emails = [
    "test@example.com",           # 올바른 이메일
    "user.name@domain.co.kr",     # 올바른 이메일
    "invalid-email@",             # @ 뒤에 도메인이 없어서 잘못됨
    "another.user@domain.com",    # 올바른 이메일
    "user@domain",                # .com 같은 점(.)과 글자가 없어서 잘못됨
    "user@domain.c",              # 마지막 부분이 한 글자라서 잘못됨
    "user@domain.company",        # 올바른 이메일
    "user123@sub.domain.com",     # 올바른 이메일
    "user+tag@domain.org",        # 올바른 이메일
    "user@domain..com"            # 점(.)이 두 번 연속 나와서 잘못됨
]

for email in emails:
    # 이메일이 맞으면 "유효함", 아니면 "유효하지 않음"을 출력해요.
    result = "유효함" if is_valid_email(email) else "유효하지 않음"
    print(f"{email}: {result}")