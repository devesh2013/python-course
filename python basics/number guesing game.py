secret = random.randint(1,50)
attempts_left = 5
won=False
print("welcome to the number guessing game!")
print("guess a secret number between 1 and 50.")
while attempts_left > 0 and not won:
    print(f"|nAttempts remaining:{attempts_left}")
guess = int(input("enter ur guess: "))
if guess==secret:
    ptint("congrats u found the secret number")
    won = True
else:
    attempts_left = 1
    diff=abs(secret - guess)
if diff <= 3:
    print("hint:hot")
elif diff <= 7 :
    print("hint:warm")
elif diff <= 15 :
    print("hint:cold")
else:
    print("hint:ice cold")
    

