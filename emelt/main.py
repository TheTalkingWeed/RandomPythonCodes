
def read_file(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

def write_file(filename,content):
    with open(filename, "w") as f:
        for i in range(len(content)):
            f.write(''.join(content[i]) + "\n")
        f.close()
    print("Kiirva.")
def main():
    foglaltasag = read_file("foglaltsag.txt")
    kategoria = read_file("kategoria.txt")


    print('1. Feladat: beolvasas')
    print(foglaltasag[0][1])
    print(kategoria)

    print('2. Feladat: ')
    sor = input("Adjon meg egy sorszamot(1-15)\n")
    hely = input("Adjon meg egy szekszamot(1-20)\n")

    if foglaltasag[int(sor)-1][int(hely)-1] == "o":
        print("Az on altal megadott hely szabad")
    else:
        print("Az on altal megadott hely foglalt")

    print("3. Feladat: ")

    eladott_jegy = 0
    oszes_hely = len(foglaltasag) * len(foglaltasag[0])
    for i in range(len(foglaltasag)):
        for j in range(len(foglaltasag[i])):
            if foglaltasag[i][j] == 'x':
                eladott_jegy += 1
    print("Az előadásra eddig ",eladott_jegy," jegyet adtak el, ez a nézőtér ",round((eladott_jegy/oszes_hely ) *100),"%-a")

    print("4. Feladat: ")
    max = 0
    for i in range(len(kategoria)):
        for j in range(len(kategoria[i])):
            if int(kategoria[i][j]) > max:
                max = int(kategoria[i][j])

    temp = [0 for i in range(max)]


    for i in range(len(kategoria)):
        for j in range(len(kategoria[i])):
                temp[int(kategoria[i][j])-1] += 1

    for i in range(len(temp)):
        if max < temp[i]: max = temp[i]
    #print(temp)
    print("A legtöbb jegyet a(z) ",temp.index(max) + 1," árkategóriában értékesítették.")

    print("5. Feladat: ")
    bevetel = 0
    for i in range(len(foglaltasag)):
        for j in range(len(foglaltasag[i])):
            if foglaltasag[i][j] == 'x':
                bevetel += 5000 if kategoria[i][j] == '1' else 4000 if kategoria[i][j] == '2' else 3000 if kategoria[i][j] == '3' else 2000 if kategoria[i][j] == '4' else 1500

    print(bevetel,"Ft")

    print("6. Feladat: ")
    ures_helyek = 0
    for i in range(len(foglaltasag)):
        for j in range(len(foglaltasag[i])-1):
            if foglaltasag[i][j] == 'o' and foglaltasag[i][j-1] == 'x'  and foglaltasag[i][j+1] == 'x':
                ures_helyek += 1
        if foglaltasag[i][0] == 'o' and foglaltasag[i][1] == 'x':
            ures_helyek += 1
        if foglaltasag[i][len(foglaltasag[i])-1] == 'o' and foglaltasag[i][len(foglaltasag[i])-2] == 'x':
            ures_helyek += 1

    print("Egyedul allo ures helyek: ",ures_helyek)

    print("7. Feladat: ")
    output  = [["0" for i in range(len(foglaltasag[0]))] for j in range(len(foglaltasag))]

    for i in range(len(foglaltasag)):
        for j in range(len(foglaltasag[i])):
            if foglaltasag[i][j] == 'o':
                output[i][j] = kategoria[i][j]
            else:
                output[i][j] = "x"

    write_file("szabad.txt",output)


if __name__ == "__main__":
    main()