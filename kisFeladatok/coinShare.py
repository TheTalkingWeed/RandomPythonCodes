def getCoinBalances(words1,words2):
    base_balance = [3,3]

    for i in range(len(words1)):
        if words1[i] == "share" and words2[i] == "share":
            base_balance[0] += 2
            base_balance[1] += 2

        if words1[i] == "share" and words2[i] == "steal":
            base_balance[0] -= 1
            base_balance[1] += 3
        if words1[i] == "steal" and words2[i] == "share":
            base_balance[0] += 3
            base_balance[1] -= 0

    return base_balance

def main():
    print(getCoinBalances(["share"], ["share"]))
    print(getCoinBalances(["steal"], ["share"]))
    print(getCoinBalances(["steal"], ["steal"]))
    print(getCoinBalances(["share", "share", "share"], ["steal", "share", "steal"]))

if __name__ == "__main__":
	main()