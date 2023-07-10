a=int(input("Enter the first Value: "))
b=int(input("Enter the second Value: "))
print(f"Before swapping the value of 'A' is {a}, and value of 'B' is {b}.")
a=a+b
b=a-b
a=a-b
print(f"After swapping the value of 'A' is {a}, and value of 'B'is {b}.")