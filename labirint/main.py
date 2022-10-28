from time import sleep
import sys


from colorama import init
from termcolor import colored

init()
def read_file(filename):
    with open (filename,"r") as f:
        return f.read().splitlines()

def print_lab(labirint):
    for i in range(len(labirint)):
        for j in range(len(labirint)):
            if labirint[i][j] == 0:
                print(colored(labirint[i][j], 'white', 'on_white'),end="")
            if labirint[i][j] == 1:
                print(colored(labirint[i][j], 'green', 'on_green'),end="")
            if labirint[i][j] == 2:
                print(colored(labirint[i][j], 'red', 'on_red'),end="")
            if labirint[i][j] == 3:
                print(colored(labirint[i][j], 'green', 'on_green'),end="")
            if labirint[i][j] == 5:
                print(colored(labirint[i][j], 'blue', 'on_blue'),end="")
            if labirint[i][j] == 9:
                print(colored(labirint[i][j], 'cyan', 'on_cyan'),end="")

        print()

def to_int_array(array):
    output = [[0 for i in range(len(array))] for j in range(len(array))]
    for i in range(len(array)):
        for j in range(len(array)):
            output[i][j] = int(array[i][j])


    return output
lab = to_int_array(read_file("labirint.txt"))

def find_start(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 3:
                return [i,j]

    return False

def find_end(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 5:
                return [i,j]

    return False

def lepes(i,j):
    if lab[i][j] != 5:
        lab[i][j] = 1

        print_lab(lab)
        print()
        sleep(.3)
        if i > 1 and  (lab[i-1][j] in [0,5]): lepes(i-1,j) # lépés felfele
        if j < len(lab[i]) and (lab[i][j+1]  in [0,5]): lepes(i,j+1) # lepes jobbra
        if j > 1 and (lab[i][j-1] in [0,5]): lepes(i,j-1) # lepes balra
        if i < len(lab) and(lab[i+1][j] in [0,5]): lepes(i+1,j) # lepes lefele

        lab[i][j] = 2
    else:
        lab[i][j] = 1


        lab[i][j] = 2
        print("kiment")
        sys.exit()



def main():

    if  find_start(lab) and find_end(lab):
        lepes(find_start(lab)[0],find_start(lab)[1])
    else:
        print("No end or starting position to the maze")


if __name__ == "__main__":
    main()