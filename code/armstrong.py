n=int(input())
a=n
s=0
while(n!=0):
    temp=n%10
    s=s+temp*temp*temp
    n=int(n/10)
   
if(s==a):
    print("yes")
else:
    print("no")    
