def sumnums(numbers):

    sum = 0
    for i in range(len(numbers)):
        sum += int(numbers[i])

    return (sum)

def main():
    print(sumnums(str(2**1000)))
    print(sumnums(str(2**15)))

if __name__ == "__main__":
    main()