#read a poem file and check whether it contains the word twinkle

f = open("poem.txt", "r")

poem = f.read()

if("twinkle".lower() in poem.lower()):
    print("Word found")
else:
    print("Word not found")

f.close()