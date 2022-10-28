def largestGap(array):

    array.sort()
    max_gap = 0
    for i in range(len(array)-1):
        if array[i+1] - array[i] > max_gap :
            max_gap = array[i+1] - array[i]

    return max_gap

def main():
    print(largestGap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]))
    print(largestGap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]))
    print(largestGap([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]))


if __name__ == "__main__":
	main()