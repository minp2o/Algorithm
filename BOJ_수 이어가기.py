firstNum = int(input())

def sooyeol(a,b):   # 첫번째 수와 두번째 수를 인자로 넣었을 때, 만들어지는 수열과 수열 길이 반환
    sy=[]
    sy.append(a)
    sy.append(b)
    nextNum=a-b
    while nextNum>=0:
        sy.append(nextNum)
        nextNum=sy[-2]-sy[-1]
    return sy,len(sy)

maxLen=float('-inf')
answer=0

for secondNum in range(1,firstNum+1):
    if sooyeol(firstNum,secondNum)[1]>maxLen:
        maxLen=sooyeol(firstNum,secondNum)[1]
        answer=secondNum
print(maxLen)
print(*sooyeol(firstNum,answer)[0])


