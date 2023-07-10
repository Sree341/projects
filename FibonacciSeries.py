count=int(input("Enter how many numbers you want to print: \n"))
num1=0
num2=1
print(num1)
print(num2)
for i in range(0,count-2):
  sum=num1+num2
  print(sum)
  num1=num2
  num2=sum


