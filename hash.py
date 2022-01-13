import hashlib
import os

# 비밀번호가 맞는지 틀린지 확인하는 함수
def check_password():
    if os.path.exists('password.txt'):
        before_password = input('비밀번호를 입력하세요:')
        m = hashlib.sha256()
        m.update(before_password.encode('utf-8'))
        with open('password.txt', 'r') as f:
            return m.hexdigest() == f.read()
        
# 만들어진 비밀번호가 없다면 새로 만들기   
if not os.path.exists("password.txt"):
    password = input('사용할 비밀번호를 입력하세요:')
    with open('password.txt', 'w') as f:
        m = hashlib.sha256()
        m.update(password.encode('utf-8'))
        f.write(m.hexdigest())

# 만들어진 비밀번호가 있다면 비밀번호 입력 요쳥하기
else:
    # 입력된 비밀번호가 맞다면 비밀번호 변경할지말지 질문하기
    if check_password():
        print("비밀번호가 일치합니다!")
        a = input("비밀번호를 변경하시겠습니까?(y/n)")
        if a == "y":
            new_password = True
        else:
            new_password = False

    # 입력된 비밀번호가 틀리면 틀렸다고 출력하기
    else:
        print("비밀번호가 일치하지 않습니다.")
        new_password = False

    # 비밀번호를 바꾸겠다고 입력받았다면 새로운 비밀번호 입력받기
    if new_password:
        with open('password.txt', 'w') as f:
            m = hashlib.sha256()
            password = input('새로운 비밀번호를 입력해주세요:')
            m.update(password.encode('utf-8'))
            f.write(m.hexdigest())