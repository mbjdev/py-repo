print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Kid tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Teenager tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("You can ride for free mate, It's on us!")	
    else:
        print("Adult tickets are $12.")
        bill = 12

    photo_option = input("Wanna take a photo? (y/n) ")
    if photo_option == "y":
        bill += 3

    print(f"Your total bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
input("\nPress Enter to Exit!")