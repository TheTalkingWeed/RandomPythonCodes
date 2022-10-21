
import math
import time


start = time.time()

pwr = [0] * 10

for i in range(0, 10) :
    pwr[i] = math.pow((float)(i), (float)(i))
def isMunchhausen(number):
    sm = 0
    temp = number

    while (temp) :
        sm= sm + pwr[(temp % 10)]
        temp = temp // 10

    return (sm == number)


def printMunchhausenNumbers(n) :
    for i in range(n) :
        if (isMunchhausen(i)) :
            print(i)

n = 10000
printMunchhausenNumbers(n)

end = time.time()

print(end - start)