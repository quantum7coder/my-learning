print("1.Prime Number Checker")
print("2.Fibonacci Series")
print("3.Prime number Checker within range")
print("4.Palindrome number Checker")
choice=int(input("Enter a choice between 1 to 4: "))
if(choice==1):
    #Prime number checker:
    num=int(input("Enter a number to check for prime: "))
    flag=True
    i=3
    if(num<=0):
        print("Enter a positive number")
    elif(num==1):
        print("1 is not prime")
    elif(num==2):
        print("2 is not a prime")
    else:
        if(num>2):    
            while(i*i<=num):
                if(num%i==0):
                    print(f"{num} is not a prime")
                    flag=False
                    break
                i+=1
        if flag:
            print(f"{num} is a prime ")
elif(choice==2):
    #First n numbers of fibbonaci sereies
    n=int(input("Enter the number of terms: "))
    a=0
    b=1
    count=0
    if(n<=0):
        print("Enter a positive number")
    elif(n==1):
        print("Fibonacci series: ")
        print(a)
    else:
        print("Fibonacci series: ")
        while(count<n):
            print(a,end=' ')
            temp=a+b
            a=b
            b=temp
            count+=1
elif(choice==3):
    #find prime numbers between given range
    a=int(input("Enter the upper bound: "))
    b=int(input("Enter the lower bound: "))
    flag=True
    for num in range(a,b+1):

        if(num<=1):
            continue
        flag=True
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                flag=False
                break
        if flag:
            print(num,end=' ')
elif(choice==4):
    #Palindrome number checker
    num=str(input("Enter a number: "))
    if(num==num[::-1]):
        print("Entered number is a palindrome")
    else:
        print("Entered number is not a palindrome")
else:
    print("You are ondho boka soda")
    