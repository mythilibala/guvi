import string
n=int(input())
m=list(map(int,input().split(" ")))
l=[]
while(len(m)!=0):
    l.append(str(max(m)))
    m.remove(max(m))
print("".join(l))    
