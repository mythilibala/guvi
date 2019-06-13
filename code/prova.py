n,q=map(int,input().split())
m=list(map(int,input().split()))
count=0
for i in range(len(m)-1):
    j=i+1
    if(m[i]+m[j]==q):
        count=1
        break
if(count):
   print("yes")
else:
   print("no")    
        
