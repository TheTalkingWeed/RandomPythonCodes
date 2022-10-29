def findOdd(array):

    temp = {}
    out = 0
    for i in array:
        temp[i] = 0

    for i in array:
        temp[i] += 1

    for i in temp.keys():
        if temp[i] % 2 == 1: out = i

    return out

def main():
    print(findOdd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
    print(findOdd([20, 1, 1, 2, 2, 3, 3, 3, 5, 5, 4, 20, 4, 5]))
    print(findOdd([10]))

if __name__ == "__main__":
	main()