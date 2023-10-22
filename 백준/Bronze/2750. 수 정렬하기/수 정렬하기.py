# 2750. 수 정렬하기

N = int(input())  # N: 수의 개수
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
for i in arr:
    print(i)