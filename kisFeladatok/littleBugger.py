def bugger(num):
    if num < 10 : return 0

    snum = str(num)
    mul = 1
    out = 0
    while len(snum) > 1:
        for ch in snum:
            mul *=  int(ch)
        snum = str(mul)
        mul = 1
        out += 1

    return out


def main():
    print(bugger(39))
    print(bugger(999))
    print(bugger(4))

if __name__ == "__main__":
	main()