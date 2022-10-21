def partreverse(list,start,end):
    return list[0:start] + list[start:end+1][::-1] + list[end+1:]


def main():
    lista = [1,2,9,6,5,8,3]
    print("alap lista: ",lista)
    print("cserélt lista:",partreverse(lista,2,4))

if __name__ =="__main__":
    main()