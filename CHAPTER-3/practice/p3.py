#detecting double spaces

#using find

message = input("Enter the message: ")

if(message.find("  ")==-1):
    print("No double space")
else:
    print("Double space exists")