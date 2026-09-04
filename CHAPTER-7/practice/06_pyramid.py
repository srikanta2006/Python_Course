#print pyramid pattern

n = int(input("Enter the number of rows: "))

for i in range(1, 4):
    print(" "*(n-i), "*"*(i*2-1))