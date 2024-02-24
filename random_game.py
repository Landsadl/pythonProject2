from random import randint


random_num = randint(1, 10)

while True:
    try:
        guess = int(input("Guess a number"))
        if guess < random_num:
            print("To low try again.")
        elif guess > random_num:
            print("To high try again. ")
        else:
            print("Great Job! ")
            break

    except ValueError:
        print("Please Enter a number: ")

print("thanks for playing")
