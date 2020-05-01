def octToDec(oct):
    lenOct = str(oct)
    le = len(lenOct)
    octal = 0
    for i in (range(le)):
        octal = octal + int(lenOct[i]) * (8 ** (le-1))
        le -=1
    print(octal)

octToDec(453)