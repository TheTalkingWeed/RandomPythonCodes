

def isAlphabeticallySorted(string):
    words = string.split(" ")

    temp = ""
    temp2 = ""
    for i in range(len(words)):
        if len(words[i]) >= 3:
            temp = list(words[i])
            temp.remove('.') if '.' in temp else 1+1
            temp2 = "".join([i for i in temp])

            temp.sort()
            if temp2 == "".join([i for i in temp]): return True

    return False

def main():
    print(isAlphabeticallySorted("Paula has a French accent."))
    print(isAlphabeticallySorted("The biopsy returned negative results.."))
    print(isAlphabeticallySorted("She sells sea shells by the sea shore."))

if __name__ == "__main__":
	main()