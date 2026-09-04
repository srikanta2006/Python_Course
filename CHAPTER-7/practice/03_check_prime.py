#check whether a number is prime

n = int(input("Enter the number: "))

flag =True
for i in range(2, n):
    if n%i ==0:
        print("Not prime")
        flag = False
        break

if flag:
    print("Is prime")
