from array import array
from asyncio.windows_events import NULL



def elso(list):
    return [list[i].upper() + "!" for i in range(len(list))]

def masodik(list):
    return [list[i][0].upper()+list[i][1:len(list[i])] for i in range(len(list))]

def harmadik():
    return [i-i for i in range(10)]

def negyedik(list):
    return [list[i]*2 for i in range(10)]

def otodik(list):
    return [int(list[i]) for i in range(10)]

def hatodik(input):
    return [input[i] for i in range(len(input))]

def hetedik(input):
    return [len(i) for i in input.split(" ")]

def nyolcadik(input):
    return [i[0] for i in input.split(" ")]

def kilencedik(input):
    return [(i,len(i)) for i in input.split(" ")]

def tizedik():
    return [i for i in range(0,10,2)]

def tizenegyedik():
    return [i*i for i in range(0,20,2)]

def tizenkettedik():
    return  [j for n, j in enumerate([i*i if i*i % 10 == 4 else 0 for i in range(0,20,2)]) if j not in [i*i if i*i % 10 == 4 else 0 for i in range(0,20,2)][:n]][1:len([j for n, j in enumerate([i*i if i*i % 10 == 4 else 0 for i in range(0,20,2)]) if j not in [i*i if i*i % 10 == 4 else 0 for i in range(0,20,2)][:n]])]

def tizenharmadik(list):
    return str(''.join(list))

def tizennegyedik(list):
    return [i.strip() for i in list]

def tizenotodik(list):
    return ''.join([str(list[i]) for i in list])

def main():
    input1 = ['auto', 'villamos', 'metro']
    print(elso(input1))

    input2 = ['aladar', 'bela', 'cecil']
    print(masodik(input2))

    print(harmadik())

    input3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(negyedik(input3))

    input4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    print(otodik(input4))
    
    input5 = "123456"
    print(hatodik(input5))

    input6 = 'The quick brown fox jumps over the lazy dog'
    print(hetedik(input6))
    
    input7 = "python is an awesome language"
    print(nyolcadik(input7))

    print(kilencedik(input6))
    
    print(tizedik())

    print(tizenegyedik())

    print(tizenkettedik())

    input8 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    print(tizenharmadik(input8))

    input9 = [' apple ', ' banana ', ' kiwi']
    print(tizennegyedik(input9))

    input10 = [1, 0, 1, 1, 0, 1, 0, 0]
    print(tizenotodik(input10))

if __name__ == "__main__":
    main()