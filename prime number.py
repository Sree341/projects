def prime_num_finder(x):
    # x=int(input("Enter the number:"))
    flag=0
    if x==1:
        print (x,"is prime not number")
    elif x==2:
        print(x,"is prime number")
    else:
        for i in range(2,x//2+2):
            flag=0
            if x%i == 0:
                print(x,"is not a prime number")
                break
            else:
                flag=1
        if flag==1:
            print(x,"is a prime number")

prime_num_finder(int(input("Enter the number:")))
