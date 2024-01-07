# 2468. 안전 영역
'''
높이는 1 이상 100 이하의 정수
안전한 영역의 최대 개수
내리는 비의 양에 따른 모든 경우를 다 조사
내리는 비의 양 -> ?

내린 비의 양 순서대로 탐색 -> 한 번 잠긴 지역은 앞으로도 계속 잠겨있음
visited가 아니라 arr에 바로 0으로 표시
아직 안 잠겼는데 방문한 곳은 visited 필요

BFS 개수는 어떻게 세는 거지?

아무 지역도 물에 잠기지 않을 수 있음
'''
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []
max_altitude = 0  # 최대 높이를 저장할 변수
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

    # 고도가 가장 높은 곳의 높이 찾기
    altitude = max(row)
    if max_altitude < altitude:
        max_altitude = altitude
'''
9
[[6, 8, 2, 6, 2],
 [3, 2, 3, 4, 6],
 [6, 7, 3, 3, 2],
 [7, 2, 5, 3, 6],
 [8, 9, 5, 2, 7]]
'''

dx = [0, 1, 0, -1]  # 우하좌상
dy = [1, 0, -1, 0]

# 비가 얼마나 왔는지 결정하기
# 비는 1 이상 max_altitued 미만으로 올 수 있음 (max_altitude이면 모두 물에 잠김)
max_zone = 0  # 안전영역의 최대 개수를 저장할 변수

for rain in range(1, max_altitude):

    # rain만큼 비가 왔을 때 안전영역의 개수를 BFS로 탐색하기
    zone = 0  # rain만큼 비가 왔을 때 안전영역의 개수를 저장할 변수
    visited = [[False] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] > rain and visited[i][j] == False:

                q.append((i, j))  # 시작점 인큐
                visited[i][j] = True  # 시작점 방문표시
                zone += 1

                while q:
                    # 디큐하기
                    x, y = q.popleft()

                    # 인큐하기
                    for d in range(4):  # 우하좌상 네 방향
                        nx, ny = x+dx[d], y+dy[d]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and arr[nx][ny] > rain:
                            q.append((nx, ny))
                            visited[nx][ny] = True

    if zone > max_zone:
        max_zone = zone

if max_zone == 0:
    print(1)
else:
    print(max_zone)