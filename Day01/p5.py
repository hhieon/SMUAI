if __name__ == '__main__':
    num1 = int(input("num1을 입력하세요 : "))
    print(num1)
    num2 = int(input("num2을 입력하세요 : "))
    print(num2)
    num3 = int(input("num3을 입력하세요 : "))
    print(num3)

    if num1 > num2 and num1 > num3:
        max = num1
        if num2 > num3:
            mid = num2
            min = num3
        else:
            mid = num3
            min = num2

    elif num2 > num3 and num2 > num1:
        max = num2
        if num1 > num3:
            mid = num1
            min = num3
        else:
            mid = num3
            min = num1

    else:
        max = num3
        if num1 > num2:
            mid = num1
            min = num2
        else:
            mid = num2
            min = num1

    print(f"최댓값은 {max}, 중간값은 {mid}, 최솟값은 {min}")