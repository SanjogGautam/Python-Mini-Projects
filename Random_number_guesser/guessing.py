import random
count=0
ans=random.randint(1,10)
print("*"*10+" Random number Guesser Game ","*"*10)
    
while True:
    try:
        n=int(input("Enter your guess(0-10)= "))
        if n==ans:
            count+=1
            print(f"You have guessed the Answer in {count} Try")
            break
        else:
            count+=1
            print("Your Guess is incorrect! Try again")
    except Exception as e:
        print(f"Error encountered = {e}")
