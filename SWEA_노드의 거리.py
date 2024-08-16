from collections import deque

#import sys
#sys.stdin=open('input.txt')

def bfs(start,end):
    q=deque()
    cnt=0
    q.append((start,cnt))
    visited[start]=True
    while q:
        cur=q.popleft()
        for nextNode in graph[cur[0]]:
            if nextNode==end:
                return cur[1]+1
            if visited[nextNode]==False:
                visited[nextNode]=True
                q.append((nextNode,cur[1]+1))



T=int(input())
for tc in range(1,T+1):
    v,e=list(map(int,input().split()))
    graph=[[] for _ in range(v+1)]
    for mm in range(e):     # [[], [4, 3], [3, 5], [], [6], [], []]
        temp=list(map(int,input().split()))
        graph[temp[0]].append(temp[1])
        graph[temp[1]].append(temp[0])

    start,end=list(map(int,input().split()))
    visited=[False]*(v+1)

    ans=bfs(start,end)
    if ans==None: print(f'#{tc} 0')
    else: print(f'#{tc} {ans}')








