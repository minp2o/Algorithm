arr=[[0]*4 for _ in range(4)]
print(all(all([i==0 for i in j]) for j in arr))

arr[1][1]=1
print(all(all([i==0 for i in j]) for j in arr))
all