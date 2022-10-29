def happy(num):

    snum = str(num)
    temp = 0
    while True:
        for i in snum:
            temp += int(i)**2

        if temp == 1 : return True
        if temp == 4 : return False

        snum = str(temp)

        temp = 0


def main():
    print(happy(203))
    print(happy(11))
    print(happy(107))


if __name__ == "__main__":
	main()