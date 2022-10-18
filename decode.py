def decode_string(string):
    out = ""

    for i in range(len(string)):

        out += decode_char(string[i]) if string[i].isalpha() else string[i]

    return out

def decode_char(char):
    return chr(ord(char)+2) if ord(char)+2 < 91 else chr(ord(char)-24) if char.isupper() else chr(ord(char)+2) if ord(char)+2 < 123 else chr(ord(char)-24)

def main():
    print(decode_string("Cbcq Dgyk!\n\nDmeybh kce cew yrwyg hmrylyaqmr:\nrylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!\n\nAqmimjjyi:\n\nYnyb"))
    


if __name__ == "__main__":
    main()