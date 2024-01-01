# 2178. 미로 탐색
'''
(1, 1)에서 (N, M)으로 이동할 때 지나야하는 최소 칸 수
배열을 이동하는 건 델타탐색으로 하는 것 같은데,
'최단거리'라는 요구사항이 있어서 BFS인가? 싶은 생각이 들었다.

델타탐색을 그리디로 수행하면 시간초과가 날 것 같아서
다른 풀이 참고해서 델타탐색과 BFS를 함께 구현하는 방법을 알아냄

주어진 행렬 자체를 일종의 그래프로 보고 BFS를 수행할 수도 있구나!

input 받는게 어려움...
'''

from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [[0] * (M+1)]  # 인덱스 맞추기 위해 추가
for _ in range(N):
    my_str = ' '.join(input())
    maze.append([0] + list(map(int, my_str.split())))

# 1. visited, q
# visited를 위한 별도의 행렬을 따로 만들지 않고, maze의 값에 경로를 바로바로 저장하기
q = deque()       # q를 덱으로 선언하기
q.append((1, 1))  # q에 시작점 인큐하고 시작 (행렬의 좌표를 저장하기)

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]

# 2. BFS 수행하기
while q:
    # 2-1. 디큐하기
    x, y = q.popleft()

    # 2-2. 인큐하기 => 여기서 그래프를 탐색할 때 델타탐색 기법을 활용
    for d in range(4):  # 동서남북 4방향
        nx, ny = x+di[d], y+dj[d]
        if 1 <= nx <= N and 1 <= ny <= M and maze[nx][ny] == 1:
            q.append((nx, ny))
            maze[nx][ny] = maze[x][y] + 1  # visited 표시와 같은 기능

print(maze[N][M])
