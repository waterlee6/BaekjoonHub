# 2566. 최댓값

# import sys
# sys.stdin = open('input.txt')
arr = [list(map(int, input().split())) for _ in range(9)]

max_val = 0  # 최대값을 저장할 변수
max_i = 0    # 최대값에서의 i값
max_j = 0    # 최대값에서의 j값
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_i = i
            max_j = j

print(max_val)
print(max_i+1, max_j+1)  # 문제의 행렬은 1행 1열 부터 시작하므로 1씩 더해줌