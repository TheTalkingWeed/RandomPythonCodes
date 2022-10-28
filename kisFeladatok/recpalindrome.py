def isPalindrome(word):

    if len(word) == 1: return True
    if len(word) == 2:  return word[0] == word[len(word)]

    if word[0] == word[-1]:
        isPalindrome(word[1:len(word)])
        return True

    return False

def main():
    print(isPalindrome("madam"))
    print(isPalindrome("adieu"))
    print(isPalindrome("rotor"))

if __name__ == "__main__":
    main()