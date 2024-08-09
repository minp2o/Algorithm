for mm in range(10):
    tcNum,edgeNum=list(map(int,input().split()))
    inputEdges = list(map(int,input().split()))
    edges = [[inputEdges[i],inputEdges[i+1]] for i in range(0,edgeNum*2,2)]
    answer=0
    def dfs(start):
        global answer
        for edge in edges:
            if start==edge[0]:
                if edge[1]==99:
                    answer=1
                    return
                dfs(edge[1])
    dfs(0)
    print(f'#{mm+1} {answer}')
