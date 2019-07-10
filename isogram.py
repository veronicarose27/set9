c=list(input())
p=[]
for i in c:
    if i not in p:
        p.append(i)
if(c==p):
    print("Yes")
else:
    print("No")
