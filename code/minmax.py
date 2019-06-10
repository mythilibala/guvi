
n=int(input())
m=list(map(int,input().split(" ")))
l=[]
while(len(m)!=0):
   if len(m)>1: 
    l.append(max(m))
    l.append(min(m))
    m.remove(max(m))
    m.remove(min(m))
   else:
       l.append(max(m))
       m.remove(max(m))
for i in l:
     print(i,end=" ")   
