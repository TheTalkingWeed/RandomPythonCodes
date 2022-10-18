def result():
    out=""
    i = 1
    while True:
        out += str(i)
        i += 1

        if len(out) >= 1000:
            out = out[990:1000]
            break

    return out


def main():
    print(result())

if __name__ == "__main__":
    main()