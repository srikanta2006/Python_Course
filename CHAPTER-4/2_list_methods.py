#list methods
#methods wont create new list, but changes the existing


list_b = [0, 3, 2, 5, 4, 6]

list_b.sort()

print(list_b)


list_b.reverse()
print(list_b)

#insert

list_b.insert(2, 35) # 35 will be present at index 2
print(list_b)

#pop at an index

list_b.pop(2)
print(list_b)

#remove an element

list_b.remove(6) #reoves element 6 

print(list_b)