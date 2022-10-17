def result(cellak):
    arr = [0 for i in range(cellak)]

    for i in range(cellak):
        print(arr)
        for j in range(i,cellak,i+1):
            arr[j] = change(arr[j])

    return arr

def change(num):
    return 0 if num == 1 else 1

def main():
    print(result(600))

if __name__ == "__main__":
    main()
