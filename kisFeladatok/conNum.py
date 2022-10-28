def cons(array):
    array.sort()

    for i in range(len(array)-1):
        if array[i+1] != array[i] + 1 :
            return False

    return True

def main():
    print(cons([5, 1, 4, 3, 2]))
    print(cons([6,7,5,8,9,4,3,2,1,0]))
    print(cons([5, 1, 4, 3, 2, 8]))
    print(cons([5, 6, 7, 8, 9, 9]))

if __name__ == "__main__":
	main()