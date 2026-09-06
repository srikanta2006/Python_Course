#readlines
f = open("file.txt", "r")
data_list = f.readlines()
print(data_list)
f.close()


#readline
f = open("file.txt", "r")
line = f.readline()
while(line!=""):
    print(line)
    line = f.readline()

f.close()
