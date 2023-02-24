# rock paper and scissor game
import random
cp_won=0
user_won=0
for i in range (5):
    arr=['rock', 'paper', 'scissor']
    a=random.randint (0,2)
    cp=arr[a]
    you=input ("Enter choice: ").lower()
    if you not in arr:
        print ("invalid option")
    else:
        if cp=='rock' and you=='scissor': #print ("computer won")
            cp_won+=1
        elif cp=='scissor' and you=='paper': #print ("computer won")
            cp_won+=1
        elif cp=='paper' and you=='rock': #print ("computer won")
            cp_won+=1
        elif cp==you:
            #print ("draw match")
            pass
        else:
            #print ("user won")
            user_won+=1
if user_won > cp_won:
    print ("user won")
elif user_won==cp_won:
    print ("draw match")
else:
    print ("computer won")
