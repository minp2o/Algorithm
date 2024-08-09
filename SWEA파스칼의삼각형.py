tc=int(input())
def dfs(l,arr):
    global n
    if l==n:
        print(' '.join(list(map(str,arr))))
        return
    nextArr=[1]*(l+1)
    print(' '.join(list(map(str,arr))))
    for i in range(1,l):
        nextArr[i]=arr[i-1]+arr[i]
    dfs(l+1,nextArr)



for mm in range(tc):
    n = int(input())
    print(f'#{mm+1}')
    dfs(1,[1])





