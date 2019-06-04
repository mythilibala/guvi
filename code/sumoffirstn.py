n,k=input().split(" ")
n=int(n)
k=int(k)

m=map(int,input().split(" "))
m=list(m)
s=0 
for i in range(k):
    s=s+m[i]
print(s)    
