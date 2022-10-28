def winRound(card1,card2):

    card1.sort()
    card2.sort()

    num1 = card1[len(card1)-1] * 10 + card1[len(card1)-2]
    num2 = card2[len(card2)-1] * 10 + card2[len(card2)-2]

    return num1>num2




def main():
    print(winRound([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]))
    print(winRound([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]))
    print(winRound([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]))
    print(winRound([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]))




if __name__ == "__main__":
	main()