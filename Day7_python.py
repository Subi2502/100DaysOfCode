#Convert a decimal to binary
print ("\nSubi - Day 7 of #100DaysOfCode\n")
print("\nDecimal to Binary\n")

def DecimalToBinary(n):
    return bin(n).replace("0b","")
if __name__=='__main__':
    print(DecimalToBinary(6537 ))

