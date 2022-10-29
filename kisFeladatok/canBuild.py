def canBuild(word1,word2):
    if len(word2) > len(word1) : return False
    if len(word2) == 0 :return True

    for ch in word2:
        if ch not in word1 :return False

    return True


def main():
    print(canBuild("aPPleAL", "PAL"))
    print(canBuild("aPPleAL", "apple"))
    print(canBuild("a", ""))
    print(canBuild("aa", "aaa"))

if __name__ == "__main__":
	main()