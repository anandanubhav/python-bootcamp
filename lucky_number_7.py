from random import randint
choice = randint(1,10)
print(f"drafted number is {choice}")
if choice == 7:
    print("You're lucky!")
else:
    print("Unlucky this time!")