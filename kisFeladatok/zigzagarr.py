from time import sleep

def zig_zag(size):
    array_out = [[0 for i in range(size)] for j in range(size)]
    curr_num = 1
    elozo_lepes  = "ale"
    i = 0
    j = 0
    array_out[0][0] = curr_num
    curr_num += 1
    while curr_num <= size ** 2:

        if i + 1 < size and (elozo_lepes == "ale" or elozo_lepes == "afel") and (j == 0 or j == size-1): # le lepes
            i += 1
            array_out[i][j] = curr_num
            curr_num += 1
            elozo_lepes = "le"

        elif j + 1 < size and (elozo_lepes == "ale" or elozo_lepes == "afel") and (i == 0 or i == size-1): # jobbra lepes
            j += 1
            array_out[i][j] = curr_num
            curr_num += 1
            elozo_lepes = "jobb"




        if elozo_lepes == "le" and j == 0: # atlo fel
            while i != 0:
                i -= 1
                j += 1
                array_out[i][j] = curr_num
                curr_num += 1
                elozo_lepes = "afel"

        elif elozo_lepes == "jobb" and i == size-1:
            while j != size-1:
                i -= 1
                j += 1
                array_out[i][j] = curr_num
                curr_num += 1
                elozo_lepes = "afel"


        if elozo_lepes == "jobb" and i == 0: # atlo le
            while j != 0:
                i += 1
                j -= 1
                array_out[i][j] = curr_num
                curr_num += 1
                elozo_lepes = "ale"

        elif elozo_lepes == "le" and j == size-1:
            while i != size-1:
                i += 1
                j -= 1
                array_out[i][j] = curr_num
                curr_num += 1
                elozo_lepes = "ale"

    return array_out


def kiir(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j],end=" \t")
        print()



def main():
    kiir(zig_zag(4 ))

if __name__ == "__main__":
	main()