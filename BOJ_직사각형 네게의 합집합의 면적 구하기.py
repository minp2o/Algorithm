lst = []
for i in range(4):
    lst.append(list(map(int, input().split())))

ch = [[0 for i in range(100)] for j in range(100)]

answer = 0
for i in range(4):
    for j in range(lst[i][0], lst[i][2]):
        for k in range(lst[i][1], lst[i][3]):
            if ch[j][k] == 0:
                answer += 1
                ch[j][k] = 1

print(answer)