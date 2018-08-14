import random
secret = random.randint(1,99)
guess = 0
tries = 0
print ("AHOY! I'm the Dread Pirate Roberts,and I have a secret!")
print ("It is a number from 1 to 99,I'll give you 6 tries.")

while guess!= secret and tries < 3:
    guess = int(input("what's your guess?"))

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")

    tries = tries + 1

    if guess == secret:
        print("Congratulate,you got it!")
    else:
        print("No more guesses! Better luck next time")

print ("The secret number is " + str(secret))

