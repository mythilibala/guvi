st,e=input().split(" ")
st=int(st)
e=int(e)
for n in range(st+1,e):

    a=n
    s=0
    while(n!=0):
        temp=n%10
        s=s+temp*temp*temp
        n=int(n/10)
   
    if(s==a):
        print(a)
