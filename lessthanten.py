def sumnums(numbers):
    lepesek = 0

    while True:
        sum = 0
        for i in range(len(numbers)):
            sum += int(numbers[i])

        numbers = str(sum)
        lepesek += 1
        if sum <=9 : break
    return (sum**lepesek)

def main():
    print(sumnums("5678688967152243674320836488841739509473801504632805087722720345618055574037062393263338500330163135756050351541309514449107970583337758483339475240522320579874511941187132217956229986675176417815239782500314657515748777313521271997092098095956126116340223644261391646169471572543357662430951144770282715888498818114686791916754895122469683089175830116365428833038587431959800219145785838153113593467001915255928243260279587053986573051564300250377055382058733121577991044324161820220380936343942009215647927537132884125886290547952062796227508292097529030269035452182908270407012319990788018004415063285820334973292514962072507997651446210867580053287297608064618496542806008419204789383772119124613183465857933712396784003461897951420018060864321768182128186608155161402875506658738548800392852484892613372857050471304637565283523602742890149959353674987209173117934744545899831765921203131367635802300784481452393567013300682653590248914706545904931601680754169053986919387778224722219716015043146"))


if __name__ == "__main__":
    main()