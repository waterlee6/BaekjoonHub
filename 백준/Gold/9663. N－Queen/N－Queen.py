# 백준 9663. N-Queen

# DFS 함수
def dfs(i):  # i: 지금 탐색하는 행 / 무조건 0부터 시작
    global ans
    # [종료조건]
    if i == N:
        ans += 1
        return

    # [수행내용]
    for j in range(N):
        if v1[j] == v2[i+j] == v3[i-j] == 0:  # (i,j)가 유효한 자리이면
            v1[j] = 1    # 방문표시
            v2[i+j] = 1
            v3[i-j] = 1

            dfs(i+1)

            v1[j] = 0    # 원상복구
            v2[i + j] = 0
            v3[i - j] = 0

N = int(input())
ans = 0

# 퀸을 놓을 수 있는지 확인할 visited 함수가 총 3개 필요함
# (위쪽, 우상향 대각선, 우하향 대각선)
v1 = [0] * N      # 열을 기록하는 visited
v2 = [0] * ((2*N)-1)  # 왜 2*N이지?
v3 = [0] * (2*N)

dfs(0)
print(ans)

