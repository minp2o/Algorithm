'''
1. 선거구 나누기 (조합)
2. 각각 선거구가 연결되어 있으면 사람 수 차이 최소 갱신
'''



from itertools import combinations


n=int(input())      # n=구역의 개수
nums=[0]*(n+1)            # 각 구역별 인간 수
tmp=list(map(int,input().split()))
for i in range(1,n+1):
    nums[i]=tmp[i-1]



graph=[[] for _ in range(n+1)]
for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    graph[i]=tmp[1:]

def bfs(start,s):
    q=[]
    q.append(start)
    cnt=1
    visited[start]=1
    while q:
        cur=q.pop(0)
        for nx in graph[cur]:
            if visited[nx]==0 and nx in s:
                visited[nx]=1
                cnt+=1
                q.append(nx)
    return cnt

miin=float('inf')
for i in range(1,n//2+1):
    for s1 in combinations([i for i in range(1,n+1)],i):
        s1=list(s1)
        s2=[i for i in range(1,n+1) if i not in s1]     # 두 선거구 조합 완성
        visited = [0] * (n + 1)

        a=bfs(s1[0],s1)
        visited = [0] * (n + 1)
        b=bfs(s2[0],s2)
        if a+b==n:
            miin=min(miin,abs(sum([nums[i] for i in s1])-sum([nums[i] for i in s2])))
if miin==float('inf'): print(-1)
else: print(miin)


