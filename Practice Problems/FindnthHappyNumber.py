rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
    sum = 0
    num1=num
    while sum != 1 and sum != 4:
        sum = 0
        while num1 != 0:
            rem = num1 % 10
            sum += (rem * rem)
            num1 //= 10
        num1 = sum

    if sum == 1:
            c+=1
            letest = num

    num = num + 1
print(rangenumber,"th Happy number is ",letest)
