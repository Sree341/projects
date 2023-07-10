def sal_fig(salary):
    salary_length=len(str(salary))
    return salary_length
print("The CEO has a " + str(sal_fig(1200000)) + "-figure salary")


num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)