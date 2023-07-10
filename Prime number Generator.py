def prime_num_gen(num):
  flag=False
  if num==1:
    (str(num)+" is not prime number")
  elif num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        flag=True
        break
    if flag:
      pass
    else:
      print(str(num) + " is prime number")
      
ini_val=0
while ini_val<200:
  prime_num_gen(ini_val)
  ini_val += 1