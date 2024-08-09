# import queue
#
#
# tc=int(input())
# n,m,k,a,b=list(map(int,input().split()))
# aTimes=list(map(int,input().split()))
# bTimes=list(map(int,input().split()))
# arriveTimes=list(map(int,input().split()))
#
# class Person:           # status는 0: 접수창구 기다리는 상태, 1: 접수창구 사용중, 2: 정비창구 기다리는 상태, 3: 정비창구 사용중 4: 끝
#     def __init__(self,cn,at,rcn,rpn,s):
#         self.customerNumber=cn
#         self.arriveTime=at
#         self.receptionNumber=rcn
#         self.repairNumber=rpn
#         self.status=s
# # 접수창고 기다리는 사람들 큐
# receptionWaiting = queue.Queue()
# # 정비창고 기다리는 사람들 큐
# repairWaiting = queue.Queue()
# # 초기 시각 t=0
# t=0
# # 접수창고 사용현황 (0이면 사용가능, n이면 남은 시간, 인덱스1에는 사용중인 사람 인스턴스)
# receptionStatus = [0,0]*a
# # 정비창고 사용현황
# repairStatus = [0,0]*b
# # 사람들 배열
# persons=[0]*(k+1)
# # 사람들 인스턴스 만들기
# for i in range(1,k+1):
#     person = Person(i,arriveTimes[i-1],0,0,0)
#     persons[i]=person
#
#
#
# # 시간은 흐른다
# while(True):
#     # 해당 시각에 정비소에 도착한 사람들 접수창구 기다리는 사람들 큐에 넣기
#     for i in range(1,k+1):
#         if persons[i].arriveTime==t:
#             receptionWaiting.put(persons[i])
#     # 기다리는 사람이 한명 이상이면, 비어있는 접수창구가 있으면 사람 넣기
#     while len(receptionWaiting)>=1:
#         if receptionStatus not in 0:    # 비어있는 접수창구가 없으면 break
#             break
#         for i in range(a):
#             if receptionStatus[i]==0:
#                 person = receptionWaiting.get()
#                 person.receptionNumber=i
#                 person.status=1
#                 receptionStatus[i]=aTimes[i]
#
#
#     # 접수창구에서 시간 끝난 사람 정비창구 웨이팅에 넣기
#
#
#
#
#

import sys
sys.stdin = open('input.txt')
import queue

# 입력 받기
# tc = int(input())
n, m, k, a, b = list(map(int, input().split()))
aTimes = list(map(int, input().split()))
bTimes = list(map(int, input().split()))
arriveTimes = list(map(int, input().split()))


# Person 클래스 정의
class Person:
    def __init__(self, cn, at, rcn, rpn, s):
        self.customerNumber = cn
        self.arriveTime = at
        self.receptionNumber = rcn
        self.repairNumber = rpn
        self.status = s


# 접수창구와 정비창구의 상태 초기화
receptionWaiting = queue.Queue()
repairWaiting = queue.Queue()
t = 0
receptionStatus = [[0, None] for _ in range(n)]
repairStatus = [[0, None] for _ in range(m)]
persons = [None] * (k + 1)

# 사람들 인스턴스 생성
for i in range(1, k + 1):
    person = Person(i, arriveTimes[i - 1], 0, 0, 0)
    persons[i] = person

# 시간 흐름 시뮬레이션
while True:
    # 접수 창구에서 기다리는 사람들 추가
    for i in range(1, k + 1):
        if persons[i].arriveTime == t:
            receptionWaiting.put(persons[i])

    # 접수 창구에서 처리
    for i in range(n):
        if receptionStatus[i][0] == 0 and not receptionWaiting.empty():
            person = receptionWaiting.get()
            person.receptionNumber = i + 1
            person.status = 1
            receptionStatus[i] = [aTimes[i], person]

    # 접수 창구에서 처리 완료된 사람들 정비 창구 대기열로 이동
    for i in range(n):
        if receptionStatus[i][0] > 0:
            receptionStatus[i][0] -= 1
            if receptionStatus[i][0] == 0:
                person = receptionStatus[i][1]
                person.status = 2
                repairWaiting.put(person)
                receptionStatus[i][1] = None

    # 정비 창구에서 처리
    for i in range(m):
        if repairStatus[i][0] == 0 and not repairWaiting.empty():
            person = repairWaiting.get()
            person.repairNumber = i + 1
            person.status = 3
            repairStatus[i] = [bTimes[i], person]

    # 정비 창구에서 처리 완료된 사람들 상태 업데이트
    for i in range(m):
        if repairStatus[i][0] > 0:
            repairStatus[i][0] -= 1
            if repairStatus[i][0] == 0:
                person = repairStatus[i][1]
                person.status = 4
                repairStatus[i][1] = None

    # 모든 사람들이 처리 완료되었는지 확인
    if all(person.status == 4 for person in persons[1:]):
        break

    # 시간 증가
    t += 1

# 특정 접수 창구와 정비 창구를 이용한 고객 번호 합산
result = sum(
    person.customerNumber for person in persons[1:] if person.receptionNumber == a and person.repairNumber == b)
if result == 0:
    result = -1

print(result)
