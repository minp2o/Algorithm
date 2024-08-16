for tc in range(1,11):
    n=input()
    q=list(map(int,input().split()))
    while 0 not in q:
        for i in range(1,6):
            if q[0]-i<=0:
                q.pop(0)
                q.append(0)
                break
            else:
                q.append(q.pop(0)-i)
    print(f'#{tc}', *q)


