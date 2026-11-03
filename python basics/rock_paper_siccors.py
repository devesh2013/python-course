import random 
while True:
    user_action = input("enter a choice (rock, paper, scissors): ")
    possible_action = ["rock", "paper" ,"scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n chose {user_actions}, computer chose {computer_actions}.\n")
    if user_action == computer_action:
        print(f"both players selected {user_actions}. its a tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes scissors u win")
        else:
            print("u looooooooooooooooooooseeeeeeee womp womp")
    elif user_action == "paper":
        if computer_action == "rock":
            print("u win")
        else:
            print("u lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("u win")
        else:
            print("u lose")
    play_again = input("play again? (y/n): ")
    if play_again != "y":
        break
          
            
        

    break
