from random import random
from random import seed



def fibonacci(n, f0=0, f1=1):
    if n == 0:
        return f0

    while n > 1:
        f0, f1 = f1, f0 + f1
        n -= 1

    return f1

seed(1)
while True:
    val = int(random()*10000)
    print(val)
    num = fibonacci(val)

    result=0

    while num > 0:
        rem = num % 10
        result = result + rem
        num = int(int(num)//10)

    print (result)
