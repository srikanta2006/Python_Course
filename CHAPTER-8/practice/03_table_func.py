#multiplication table using reccursion

def table(i, n):
    if(i==11):
        return
    print(f'{n} x {i} = {n*i}')
    table(i+1, n)

def tab(n):
    table(1, n)

n=int(input("Enter the number: "))
tab(n)

