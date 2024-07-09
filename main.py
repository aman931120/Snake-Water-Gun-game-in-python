'''
1 for snake
-1 for water
0 for gun
'''

import random
computer = random.choice([-1,0,1])
you=input("enter your choice = ")
gameDict={
    "s":1,
    "w":-1,
    "g":0
}

youNum=gameDict[you]
# print(youNum)
revDict={
    1:"Snake",
    -1:"Water",
    0:"gun"
}

print("you choosed = ",revDict[youNum])
print("computer choosed = ",revDict[computer])

if(computer==youNum):
    print("Its a draw")
else:
    if(computer==1 and youNum==-1):
        print("You loose! try again")
    elif(computer==1 and youNum==0):
        print("You Win!")
    elif(computer==-1 and youNum==1):
        print("You Win!")
    elif(computer==-1 and youNum==0):
        print("You loose! try again")
    elif(computer==0 and youNum==-1):
        print("You Win!")
    elif(computer==0 and youNum==1):
        print("You loose! try again")


