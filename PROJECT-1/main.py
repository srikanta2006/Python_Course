'''
SNAKE WATER GUN GAME!!
1 - snake
-1 - water
0 - gun
'''
import random

ruleDict = {'s' : 1, 'w': -1, 'g': 0}
revDict = { 1 : 'snake', -1 : "Water", 0: "Gun"}
computer = random.choice([-1, 0, 1])

print("choices : s, w, g")
user = input("Enter your choice: ")

yc = ruleDict[user] 

print(f'You choose {revDict[yc]} and computer choose {revDict[computer]}')


score = computer-yc
if(computer==yc):
    print("It's a Draw!")
elif(score==-1 or score==2):
    print("You Lose!")
else:
    print("You Win!")