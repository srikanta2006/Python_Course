#update the high score file 

import random

def game():
    return random.randint(1,62)

f = open("High_Score.txt", "r")
high_score = f.read()
score =game()
if(high_score=="" or int(high_score)<score):
    fw = open("High_Score.txt", "w")
    fw.write(str(score))
    fw.close()

f.close()
