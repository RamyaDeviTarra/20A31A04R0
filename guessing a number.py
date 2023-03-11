import random
n = random.randrange(1,100)
guess = int(input("enter the value"))
while n!=guess:
    if guess<n:
        print("too low")
        guess = int(input("enter the value"))
    elif guess>n:
        print("too high")
        guess = int(input("enter the value"))
    else:
        break
print("your guessed it right")    
