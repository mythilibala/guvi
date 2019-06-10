import string
s,n=input().split(" ")
n=int(n)
s=s[-1:-n-1:-1]
k=[]
for i in range(len(s)-1,-1,-1):
    k.append(s[i])
print("".join(k))    
   
