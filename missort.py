p=int(input())
u=list(map(int,input().split()))
for i in range(p-1):
    if(u[i]>u[i+1]):
        print(i)
        
