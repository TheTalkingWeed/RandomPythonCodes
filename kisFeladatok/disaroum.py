def isDisarium(number):
    snum = str(number)
    temp = 0
    for i in range(len(snum)):
        temp += int(snum[i])**(i+1)

    return temp == number



def main():
    print(isDisarium(75))
    print(isDisarium(135))
    print(isDisarium(544))
    print(isDisarium(518))
    print(isDisarium(8))
    print(isDisarium(466))

if __name__ == "__main__":
	main()