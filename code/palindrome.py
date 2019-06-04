n=input()
if(int(n)<=1000):
    if(n==n[::-1]):
        print("yes")
    else:
        print("no")
