
tc = int(input())
for t in range(tc):
    n=int(input())
    scores = [list(map(int,input().split())) for _ in range(n)] # 먹이 테이블
    dx=[-1,0,1,0]   #상하좌우
    dy=[0,-1,0,1]
    maax=float('-inf')  #최대 먹을 수 있는 양
    temp=0
    for i in range(n):
        for j in range(n):  # 모든 셀을 돌면서 최대값 갱신

            temp+=scores[i][j]      # 각 셀의 먹을 수 있는 양 더하기
            for k in range(4):  #   상하좌우 더하기
                nx = i + dx[k]
                ny = j + dy[k]
                if(0<=nx<n and 0<=ny<n):    #테이블을 벗어나는지 확인
                    temp+=scores[nx][ny]
            if temp<0:  # 합계가 음수인 경우
                if -(temp)<maax: maax = temp    #절댓값으로 변환해서 최대값 갱신
            if temp>=maax: maax = temp
            temp=0
    print(f'#{t+1} {maax}')

