import random

# Python khud ek random number soch lega 1 se 100 ke beech
number_to_guess = random.randint(1, 100)
attempts = 0

print("Maine 1 se 100 ke beech ek number socha hai. Guess karo!")

while True:
    guess = int(input("Apna guess likho: "))
    attempts += 1

    if guess < number_to_guess:
        print("Thoda aur bada number try karo!")
    elif guess > number_to_guess:
        print("Thoda chhota number try karo!")
    else:
        print(f"Sahi jawab! Number tha: {number_to_guess}")
        print(f"Aapne {attempts} attempts mein guess kiya.")
        break
