#find greatest of 3 numbers using function


def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print(greatest(1,2,3))