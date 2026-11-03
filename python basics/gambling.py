import random 
playing = True
number = str(random.randint(0,9))
print("i will give 0 to 9 and u have to guess which number i picked")
print("the game ends when u get 1 hero!")
while playing:
    guess = input("give me ur best guess! \n")
    if number == guess:
        print("u win the game")
        print("the number was",number)
        break
    else:
        print("u gues is wrong,try again.\n")
 