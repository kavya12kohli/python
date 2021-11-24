n=int(input("Enter the number of terms:"))
n1=0
n2=1

if n<=0:
    print("Incorrect attempt")
elif n==1:
    print("Your Fibonacci numbers are:")
    print(n1)
else:
    print("Your Fibonacci numbers are:")
    print(n1)
    for numbers in range(0,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n1)
