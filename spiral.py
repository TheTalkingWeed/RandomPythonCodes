def spiral(size):
    spiral_array = [[0 for i in range(size)] for j in range(size)]
    curr_num = 1
    start = 0
    end = size

    while curr_num != size ** 2+1:
        for j in range(start,end):
            spiral_array[start][j]  = curr_num
            curr_num +=1
        start += 1


        for i in range(start,end):
            spiral_array[i][end-1] = curr_num
            curr_num += 1
        start -= 1

        for j in range(end-2,start-1,-1):
            spiral_array[end-1][j] = curr_num
            curr_num += 1

        for i in range(end-2,start,-1):
            spiral_array[i][start] = curr_num
            curr_num += 1

        start += 1
        end -= 1

    return spiral_array

def kiir(tomb):
    for i in range(0,len(tomb)):
        for j in range(0,len(tomb[i])):
            print(tomb[i][j],"\t",end="")
        print("\n",end="")
def main():
    while True:
        kiir(spiral(int(input("Add meg: "))))


if __name__ == "__main__":
    main()