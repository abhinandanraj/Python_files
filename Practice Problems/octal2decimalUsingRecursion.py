decimal=0
sem=0
def OctalToDecimal(n):
    global sem,decimal
    if(n!=0):
        decimal+=(n%10)*pow(8,sem)
        sem+=1
        OctalToDecimal(n // 10)
    return decimal
n=int(input("Enter the Octal Value:"))
print("Decimal Value of Octal number is:",OctalToDecimal(n))
