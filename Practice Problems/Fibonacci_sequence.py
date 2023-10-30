n = int(input("Number of terms = "))

# first two terms
n1, n2 = 0, 1
count, total = 0, 0

# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")

# if there is only one term, return n1
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)

# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       total += n1
       # update values
       n1 = n2
       n2 = nth
       count += 1
       

print("Sum of fibonacci sequence upto n =", total)