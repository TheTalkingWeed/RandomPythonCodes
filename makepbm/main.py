from functions import *

def main():
    input = read_file("binaryinput.txt")
    new_size = get_primes(len(input))
    print(len(read_file("binaryinput.txt")))
    print(new_size)
    resized_input = resize(new_size[0],new_size[1],input)
    print(resized_input)
    write_file("output.pbm",resized_input,new_size[0],new_size[1])
if __name__ == "__main__":
    main()