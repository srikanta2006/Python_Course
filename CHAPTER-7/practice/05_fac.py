#factorial of a number

n = int(input("Enter the number: "))

prod=1
for i in range(n, 1, -1):
    prod*=i

print(prod)