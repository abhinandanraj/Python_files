import math
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
    num1=num
    c1 = 0
    num2 = num
    while num1 != 0:
        num1 //= 10
        c1 += 1
    num1 = num
    sum = 0
    while num1 != 0:
        rem = num1 % 10
        sum += math.pow(rem, c1)
        num1 //= 10
        c1 -= 1
    if sum == num2:
            c+=1
            letest = num

    num = num + 1
print(rangenumber,"the Disarium  number is ",letest)
