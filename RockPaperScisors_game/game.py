import random
l = ["rock", "paper", "scissors"]


def cont():
    y = input("Do you want to continue(yes/no?)= ")
    if y.lower() == "yes":
        return True
    else:
        print("*"*10+" Exiting "+"*"*10)
        return False


while True:
    comp = random.choice(l)
    user = input("Enter Rock,Paper or Scissors= ").lower()
    if user in l:
        if comp == user:
            print("*"*10+" Draw "+"*"*10)
        elif (comp == "rock" and user == "scissors") or (comp == "paper" and user == "rock") or (comp == "scissors" and user == "paper"):
            print("*"*10+" Computer wins "+"*"*10)
        else:
            print("*"*10+" User wins "+"*"*10)
        if cont():
            continue
        else:
            break
    else:
        print("*"*10+" You have entered the wrong input "+"*"*10)
        
 
