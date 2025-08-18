import math
from random import random, randint

if __name__ == '__main__':
    a = 10
    b = 20
    c = 3.14
    print(math.floor(c))
    #print(random()) # 0.0 ~ 0.9999999
    print(int(random() * 10) + 1) # 1 ~ 10
    print(randint(1, 10))

    if a == b:
        print("OK")
    else:
        print("Fail")
