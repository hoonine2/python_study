def register_user():
    print('function_test')
    print('===============')
    print('회원가입')
    print('===============')

    register = False

    while not register:
        print('회원가입을 진행하시겠습니까?\n y:진행    N:취소')
        register_input = input('>> ')
        register_input = register_input.lower()

        if register_input == 'y':
            register = True
            print('===============')
            print('회원가입')
            print('===============')
        elif register_input == 'n':
            print('===============')
            print('회원가입 취소')
            print('===============')
            exit()
        else:
            print('입력값을 확인해주세요')

        users = []

        while True:

            user = {}

            username = input('ID: ')
            while True: 
                pw = input('PW: ')
                pw_confirm = input('PW 확인: ')
                if pw == pw_confirm:
                    break
                else:
                    print('일치하지 않습니다.')
            name = input('이름: ')
            while True:
                birth_date = input('생년월일 6자리: ')
                if len(birth_date) == 6:
                    break
                else:
                    print('생년월일이 올바르지 않습니다.')
            email = input('이메일: ')

            user['username'] = username
            user['pw'] = pw
            user['name'] = name
            user['birth_date'] = birth_date
            user['email'] = email

            users.append(user)
            print(users)


            print("-----------")
            print(f"{user['name']}님 가입을 환영합니다.")
            print("-----------")

            print('회원가입을 추가로 진행하시겠습니까? \n Y:진행    N:취소')
            register_another_input = input('>> ')
            register_another_input.lower()

            if register_another_input == 'y':
                pass
            elif register_another_input == 'n':
                print('안녕히가세요.')
                exit()


