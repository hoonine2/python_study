day = input("요일을 입력해주세요(0~6): ")

if day == "0":
    print("휴무")
elif day == "6":
    print("단축영업")
else:
    print("정상영업")