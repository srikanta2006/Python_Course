#compute factorial of n using reccursion

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)




n = int(input("Enter the number: "))

print(fac(n))