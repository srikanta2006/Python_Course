#max of 4 input numbers
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a>b and a>c and a>d):
    print(a, "is greatest")

elif(b>a and b>c and b>d):
    print(b, "is greatest")

elif(c>a and c>b and c>d):
    print(c, "is greatest")
else:
    print(d, "is greatest")