#number series 0,0,7,6,14,12,21,18,28,24....wrtite a program for given series
n = int(input("enter the value"))
if n%2==0:
    n=n//2
    print(n*6)
else:
    n=n//2+1
    print(n*7)
