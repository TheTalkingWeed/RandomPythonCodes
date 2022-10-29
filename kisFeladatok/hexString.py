def firstIndex(coded_string,string):

    return bytes.fromhex(coded_string).decode('utf-8').find(string)


def main():
    print(firstIndex("68 65 6c 6c 6f 20 77 6f 72 6c 64", "world"))
    print(firstIndex("47 6f 6f 64 62 79 65 20 77 6f 72 6c 64", "world"))
    print(firstIndex("42 6f 72 65 64 20 77 6f 72 6c 64", "Bored"))

if __name__ == "__main__":
	main()