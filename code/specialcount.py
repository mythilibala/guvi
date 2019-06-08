n=input()
count=0
for i in range(len(n)):
    if(n[i]>='0'and n[i]<='9'):
        continue
    elif(n[i]>='A' and  n[i]<='Z'):
        continue
    elif(n[i]>='a' and  n[i]<='z'):
        continue
    else:
        count=count+1
    
print(count)        
