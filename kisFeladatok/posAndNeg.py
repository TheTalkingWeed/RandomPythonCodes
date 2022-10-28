def alternateSign(array):

    for i in  range(0,len(array),2):
        array[i] = array[i] * -1

    return True if all(x >= 0 for x in array) or all(x <= 0 for x in array) else False

def main():
    print(alternateSign([3, -2, 5, -5, 2, -8]))
    print(alternateSign([-6, 1, -1, 4, -3]))
    print(alternateSign([4, 4, -2, 3, -6, 10]))

if __name__ == "__main__":
	main()