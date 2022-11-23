import random

answer = random.randint(1, 20)
guess = int(input("enter the number: "))

while guess != answer:
    print("wrong try again!")

    if guess < answer:
        print("guess higher")

    elif guess > answer:
            print("guess lower")
    guess = int(input("enter the number: "))

if guess == answer:
    print("YOU GOT IT RIGHT ! ! !")
else:
    print("you are wrong ")