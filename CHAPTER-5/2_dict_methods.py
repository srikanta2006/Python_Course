#dictionary methods

marks = {
    "Srikanta" : 100,
    "Abhinav" : 90,
    "Vrushank" : 85
}

# .items
print(marks.items())

# .keys()

print(marks.keys())

#.values()

print(marks.values())

# .update() -> updates the value to a key if it exists, if not then creates a new key 

marks.update({"Srikanta" : 99})

# .get()

print(marks.get("Sri")) # does not return error is key not exists, rather returns None

print(marks["Sri"]) # returns error