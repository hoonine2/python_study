def get_id(email):

    if email.endswith('@abc.com'):
        email_id = email.removesuffix('@abc.com')
        print(email_id)
        return email_id
    else:
        print('처리할 수 없는 주소입니다.')