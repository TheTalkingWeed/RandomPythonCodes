def isFactorial(num):
    temp = 1
    i = 1
    while temp < num:
        temp *= i
        if temp == num: return True

        i +=1
    return False

def main():
    print(isFactorial(2))
    print(isFactorial(27))
    print(isFactorial(24))
    print(isFactorial(120))

if __name__ == "__main__":
    main()