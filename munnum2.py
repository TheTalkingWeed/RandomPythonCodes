
import math
import time
asd
start = time.time()

def isMunchhausen(number):
    return number == sum(int(x) ** int(x) for x in str(number))
    

def printMunchhausenNumbers(n) :
    for i in range(n) :
        if (isMunchhausen(i)) :
            print(i)
            
        
 

n = 10000
printMunchhausenNumbers(n)

end = time.time()

print(end - start)