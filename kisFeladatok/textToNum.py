def convert(char):
    char = char.upper()
    return  "2" if char in "ABC" else \
            "3" if char in "DEF" else \
            "4" if char in "GHI" else \
            "5" if char in "JKL" else \
            "6" if char in "MNO" else \
            "7" if char in "PQRS" else \
            "8" if char in "TUV" else \
            "9"

def textToNum(input):
    nums="0123456789-()"
    out = ""
    for i in range(len(input)):
        if input[i] not in nums:
            out += convert(input[i])
        else: out += input[i]

    return out


def main():
    print(textToNum("123-647-EYES"))
    print(textToNum("(325)444-TEST"))
    print(textToNum("653-TRY-THIS"))
    print(textToNum("435-224-7613"))

if __name__ == "__main__":
	main()