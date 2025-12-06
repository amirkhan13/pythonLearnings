import random 
import sys

def Guess_the_Number():
    Comp_num = random.randint(1,100)
    attempts = 5
    
    while attempts > 0:
        guess = int(input("Enter your guess (between 1 and 100): "))
        
       
        if guess < 1 or guess > 100:
            print("Please enter a number within the range of 1 to 100.")
            continue
        
       
        if guess == Comp_num:
            print("Your Guess is Correct! You Win!!!")
            sys.exit()
        
      
        attempts -= 1
        print("Oops! Your guess was Wrong!!!")
        
        if attempts > 0:
            print(f"You have {attempts} attempts left!!!")
           
        else:
            print(f"Attempts over! The computer's number was {Comp_num}. Try again!")
            sys.exit()

Guess_the_Number()
