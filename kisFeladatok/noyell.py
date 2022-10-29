def noYell(string):
    words = string.split(" ")


    words[len(words)-1] = words[len(words)-1][0:words[len(words)-1].find("?")+1] if words[len(words)-1][-1] == "?" else \
    words[len(words)-1][0:words[len(words)-1].find("!")+1] if words[len(words)-1][-1] == "!" else words[len(words)-1]

    return " ".join(i for i in words )


def main():
    print(noYell("What went wrong?????????"))
    print(noYell("Oh my goodness!!!"))
    print(noYell("I just!!! can!!! not!!! believe!!! it!!!"))
    print(noYell("Oh my goodness!"))
    print(noYell("I just cannot believe it."))

if __name__ == "__main__":
	main()