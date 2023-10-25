print("Enter the octal number: ");
octal=int(input());
decimal = 0
sem = 0
while(octal!= 0):
        decimal=decimal+(octal%10)*pow(8,sem)
        sem+=1
        octal=octal// 10
print("Decimal number is: ",decimal)
