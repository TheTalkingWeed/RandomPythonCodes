

def warOfNumbers(list):
    soo = 0
    soe = 0

    for i in list:
        if i % 2 == 0 :soe += i
        if i % 2 != 0 :soo += i

    return soe - soo if soe > soo else soo - soe

def warOfNumbers2(list):
    out = 0

    for i in list:
        if i % 2 == 0 :
            out -= i
        else :out += i

    return abs(out)

def warOfNumbers3(list):

    return abs([ ])



def main():
    print(warOfNumbers([2, 8, 7, 5]))
    print(warOfNumbers([12, 90, 75]))
    print(warOfNumbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))

    print(warOfNumbers2([2, 8, 7, 5]))
    print(warOfNumbers2([12, 90, 75]))
    print(warOfNumbers2([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))

if __name__ == "__main__":
	main()