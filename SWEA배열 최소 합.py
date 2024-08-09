import sys
sys.stdin=open('input.txt')
def dfs(l):
    global combi,MIN
    if l==n:
        temp=0
        for j in range(n):
            temp+=arr[j][combi[j]]
        if temp<MIN:
            MIN=temp
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            combi[l]=i
            dfs(l+1)
            visited[i]=0



tc=int(input())
for mm in range(tc):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    combi=[0]*n
    visited=[0]*n
    MIN=float('inf')
    dfs(0)
    print(f'#{mm+1} {MIN}')
