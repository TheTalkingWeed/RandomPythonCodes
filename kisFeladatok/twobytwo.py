def swapTwo(string):
    out = ""
    for i in range(0,len(string)-len(string) % 4,4):
        out += string[i+2:i+4] + string[i:i+2]

    return out + string[(len(string)-len(string) % 4):]

def main():
    print(swapTwo("ABCDEFGH"))  #CDABGHEF
    print(swapTwo("AABBCCDDEEFF"))  #BBAADDCCFFEE
    print(swapTwo("munchkins")) #ncmuinhks
    print(swapTwo("FFGGHHI"))   #GGFFHHI

if __name__ == "__main__":
	main()