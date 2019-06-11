n=int(input())
reverse=0
while(n!=0):
    temp=n%10
    reverse=reverse*10+temp
    n=int(n/10)
print(reverse)    
    
