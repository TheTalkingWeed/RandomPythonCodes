def read_file(filenae):
    with open(filenae, "r") as f:
        contents = f.read()
    return contents

def write_file(filename,content,width,height):
    with open(filename,"w") as f:
        f.write("P1\n")
        f.write("# output.pbm\n")
        f.write(str(width) +" ")
        f.write(str(height) + "\n")


        for i in range(len(content)):
            f.write(''.join(content[i]) + "\n")
        f.close()
    print("kiirva")

def get_primes(size):
    temp = 1

    while True:
        if is_prime(temp) and is_prime(round(size/temp)):
            return [temp,round(size / temp)]
        temp += 1



def resize(width,heigth,input):
    output = [[0 for i in range(width)] for j in range(heigth)]
    temp = 0
    for i in range(heigth):
        for j in range(width):
            output[i][j] = input[temp]
            temp += 1


    return output

def is_prime(number):

    temp = False

    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                temp = True
                break
    return True if not temp else False

