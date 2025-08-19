if __name__ == '__main__':
    # set
    print("==set==")
    t1 = {1, 2, 3, 4, 5}
    print(type(t1))
    print(t1)
    t1.add(6)
    t1.add(5)
    print(t1)

    # tuple
    print("==tuple==")
    t2 = (1, 2, 3, 4, 5)
    print(type(t2))
    print(t2)
    print(t2[1])

    # dictionary, key:value
    # JavaScript JSON
    print("==dictionary==")
    d1 = {'a':1, 'b':2, 'c':3}
    print(type(d1))
    print(d1)
    print(d1['a'])

    d2 = {"name":"최혜주", "age":22, "major":"security"}
    print(d2["name"])
    print(d2["age"])

    # 응용
    sts = [
        {"name": "최혜주", "age": 22, "major": "security"},
        {"name": "이나연", "age": 21, "major": "security"},
        {"name": "김나현", "age": 21, "major": "security"},
        {"name": "윤서진", "age": 23, "major": "security"},
        {"name": "이신우", "age": 21, "major": "chemistry"}
    ]

    # 전체 학생 들의 나이의 합과 평균
    ageSum = 0
    for i in sts:
        ageSum += i["age"]
    ageAve = ageSum / len(sts)
    print(f"나이의 합 : {ageSum}, 나이 평균 : {ageAve}")

    # security 학과 학생 들의 나이의 합과 평균
    seAgeSum = 0
    cnt = 0
    for j in sts:
        if j["major"] == "security":
            seAgeSum += j["age"]
            cnt += 1
    seAgeAve = seAgeSum / cnt
    print(f"나이의 합 : {seAgeSum}, 나이 평균 : {seAgeAve}")