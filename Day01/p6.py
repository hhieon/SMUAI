if __name__ == '__main__':
    num1 = int(input("num1을 입력하세요 : "))
    print(num1)
    num2 = int(input("num2을 입력하세요 : "))
    print(num2)

    if num1 > num2:
        max = num1
        min = num2

    else:
        max = num2
        min = num1

    print(f"최댓값은 {max}, 최솟값은 {min}")