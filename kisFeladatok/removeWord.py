def removeWord(sentence,word):

    splitted = sentence.split(" ")

    return " ".join([i for i in splitted if i != word])

def main():
    print(removeWord("One two three four", "two"))
    print(removeWord("Bob has a kid", "kid"))

if __name__ == "__main__":
	main()