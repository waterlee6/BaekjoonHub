# 2738. 행렬 덧셈

# import sys
# sys.stdin = open('input.txt')
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# print(A)
# print(B)
ans = []  # 답을 담을 빈 리스트
for i in range(N):
    temp = []  # 한 행을 임시로 담을 빈 리스트
    for j in range(M):
        temp.append(A[i][j] + B[i][j])
    ans.append(temp)

for row in ans:
    print(*row)
