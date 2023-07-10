print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?\n"))
bill=0

if height >=120:
    print("You can ride the rollercoaster!")
    age=int(input("What is your age?\n"))
    if age<12:
        print("Child tickets are $5.")
        bill+=5
    elif age<=18:
        print("Youth tickets are $7.")
        bill+=7
    elif age>=45 and age<=55:
        print("No charge for you")
        bill+=0
    else:
        print("Adult tickets are $12")
        bill+=12
    want_photos=input("Do you want photos taken? Y or N.\n")
    if want_photos=="Y":
        bill+=3
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry you can't ride the rollercoaster.")