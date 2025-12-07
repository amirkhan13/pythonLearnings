import random


def start_game():
    user_score=0
    comp_score=0
    

    rounds = 5

    while rounds>0:
        user_choice =input("choose rock,paper or scissors:").lower()
        comp_choice = random.choice(["rock" ,"paper", "scissors"])

        if user_choice == comp_choice:
            print("It's a draw")
            rounds = rounds -1
            print(f"your score is {user_score} ")
            print(f"comp score is {comp_score} ")
            print(f"Rounds left {rounds}")
        elif user_choice =="rock" and comp_choice =="scissors":
            print("You Won!!")
            print(f"computer's choice was {comp_choice}")
            user_score+=1
            print(f"your score is {user_score} ")
            print(f"comp score is {comp_score} ")
            rounds = rounds -1
            print(f"Rounds left {rounds}")
        elif user_choice == "paper" and comp_choice =="rock":
            print("You Won!!")
            print(f"computer's choice was {comp_choice}")
            user_score+=1
            print(f"your score is {user_score} ")
            print(f"comp score is {comp_score} ")
            rounds = rounds -1
            print(f"Rounds left {rounds}")
        elif user_choice == "scissors" and comp_choice =="paper":
            print("You Won!!!")
            print(f"computer's choice was {comp_choice}")
            user_score+=1
            print(f"your score is {user_score} ")
            print(f"comp score is {comp_score} ")
            rounds = rounds -1
            print(f"Rounds left {rounds}")
        else:
            print("Oops!! You Lost")
            print(f"computer's choice was {comp_choice}")
            comp_score = comp_score+1
            print(f"your score is {user_score} ")
            print(f"comp score is {comp_score} ")
            rounds = rounds -1
            print(f"Rounds left {rounds}")

    print("\n--- Game Over ---")
    if user_score > comp_score:
        print("Congratulations! You won the game!")
    elif comp_score > user_score:
        print("Sorry! Computer won the game!")
    else:   
        print("It's a tie!")
start_game()


    

    