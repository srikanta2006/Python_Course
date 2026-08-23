translator = {"ela unnav" : "How are you", 
              "thinnava" : "Did you eat",
              "paduko" : "Go to sleep"}

print("Words you can choose", translator.keys())

word = input("Type the word to translate: ")

print(translator.get(word))
