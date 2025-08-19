import pickle

if __name__ == '__main__':
    sts = [
            {"name": "최혜주", "age": 22, "major": "security"},
            {"name": "이나연", "age": 21, "major": "security"},
            {"name": "김나현", "age": 21, "major": "security"},
            {"name": "윤서진", "age": 23, "major": "security"},
            {"name": "이신우", "age": 21, "major": "chemistry"}
        ]

    pickle.dump(sts, open("data/sts.pkl", "wb"))
    result = pickle.load(open("data/sts.pkl", "rb"))
    print(type(result))
    print(result)