def toCamelCase(string):

    temp = string.split("_")
    out= temp[0]
    for i in range(1,len(temp)):
       out += temp[i].capitalize()
    return out

def toSnakeCase(string):

    out = ""
    for i in range(len(string)):
        if not string[i].isupper():
            out += string[i]
        else:
            out += "_" + string[i].lower()

    return out
def main():
    print(toCamelCase("hello_edabit"))
    print(toSnakeCase("helloEdabit"))
    print(toCamelCase("is_modal_open"))
    print(toSnakeCase("getColor"))

if __name__ == "__main__":
	main()