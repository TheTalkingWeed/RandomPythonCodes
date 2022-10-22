from enum import Enum

class Hang(Enum):
    MELY  = 1
    MAGAS = 2
    VEGYES = 3
    SEMILYEN = 4

def hangzas(szo):
    mely = "aáoóuú"
    magas =  "eéiíöőüű"

    isMely = False
    isMagas = False

    for i in mely:
        if i in szo:
            isMely = True
            break
    for i in magas:
        if i in szo:
            isMagas = True
            break

    return Hang.VEGYES.name if isMely and isMagas else Hang.MELY.name if \
            isMely else Hang.MAGAS.name if isMagas else Hang.SEMILYEN.name

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély","Pfffffff"]

    for i in words:
        print(hangzas(i))



if __name__ == "__main__":
	main()