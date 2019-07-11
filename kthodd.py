y,u=map(int,input().split())
count=0
t=list(map(int,input().split()))
for i in t:
    if(i%2!=0):
        count=count+1
    if(count==u):
        print(i)
        break
