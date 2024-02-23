# 2573. 빙산
'''
일년마다 동서남북 네 방향으로 붙어있는 0 칸 개수만큼 높이가 감소
빙산이 두 덩어리 이상으로 분리되는 최초의 시간
전부 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0을 출력

1. 1년이 지날 때마다 빙하를 녹이기 -> 델타탐색
2. 몇 개의 덩어리로 분리되었는지 확인하기 -> BFS 
'''
from pprint import pprint
from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 델타탐색 방향
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


# 빙하 주변의 바다를 찾는 함수
def finding(arr, surroundedby):
    for i in range(N):
        for j in range(M):
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]

                # 벽 세우기
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] <= 0 and arr[i][j] > 0:
                    surroundedby[i][j] += 1


# 빙하를 녹이는 함수
# 더 이상 녹일 빙하가 없을 때를 구분하는 flag를 return 하도록 작성 
def melting(arr, surroundedby):
    no_more_melting = True  # 더 이상 녹일 빙하가 없는지 확인 위한 변수(매번 True로 초기화)
    for i in range (N):
        for j in range(M):
            if surroundedby[i][j] != 0 and arr[i][j] > 0:
                no_more_melting = False   # 하나라도 녹이면 녹일 빙하가 있는 것 
                arr[i][j] -= surroundedby[i][j]
    return no_more_melting


# 몇 개의 덩어리인지 확인하는 함수
year = 0     # 연도를 셀 변수 

def counting():
    global arr, year
    enough_iceburg = False  # 빙하의 개수가 2개 이상임 확인 위한 변수 
    # year = 0  # global 변수 year를 초기화
    # print('year +1 ===============')

    while enough_iceburg == False:
        year += 1
        # print('새로운 arr 탐색 시작 ==================')
        # pprint(arr)
        visited = [[0] * M for _ in range(N)]
        q = deque()
        enough_iceburg = False    # 빙산의 개수를 셀 변수
        iceburg = 0

        surroundedby = [[0] * M for _ in range(N)]  # 주위 바다의 개수를 표시할 배열(매번 초기화)

        finding(arr, surroundedby)
        # print('finding 함수 실행')
        # pprint(surroundedby)

        # no_more_melting = True  # 더 이상 녹일 빙하가 없는지 확인 위한 변수(매번 True로 초기화)
        no_more_melting = melting(arr, surroundedby)
        # melting(arr, surroundedby)
        # print('melting 함수 실행')
        # pprint(arr)
        # print(no_more_melting)

        # 빙하가 다 녹을 때까지 빙하가 2개 미만인 경우 탈출 조건
        # print('iceburg', iceburg)
        if no_more_melting == True or iceburg >= 2:
            # print('no_more_melting 탈출==========')
            break  # while문 탈출 
        
        while enough_iceburg == False:
            # 1. 아직 방문하지 않은 빙하 찾아서 q에 넣기
            # print('search 들어옴')
            # print(enough_iceburg)
            start_search = False   # 탐색을 시작할 첫번째 빙하를 찾았는지 확인 위한 변수
            for i in range(N):
                for j in range(M):
                    if arr[i][j] > 0 and visited[i][j] == 0:
                        q.append((i, j))
                        visited[i][j] = 1    # 디큐할 때가 아니라 인큐할 때 방문처리 
                        # print(f'{(i, j)}번째 좌표 찾음')
                        iceburg += 1         # 새로운 지점 찾을 때 iceburg +1
                        if iceburg >= 2:
                            enough_iceburg = True
                        # print('iceburg +1')
                        start_search = True  # 탐색을 시작할 첫번째 빙하를 찾으면 for문 break
                        break
                if start_search == True:
                    break  # for문 break
            else:   # for문을 다 도는 동안 start_search가 False이면 더 이상 탐색할 빙하 없음 
                # print('못 찾아서 끝남')
                # no_more_search = True
                break  # while문 break??

            # 2. start_search=True일 때 연결된 빙하들을 찾아서 q에 넣고 방문표시 하기
            # print(f'여기까지는 옴 {q}')
            while q:
                i, j = q.popleft()
                # print(f'{(i, j)}를 탐색')
                for d in range(4):
                    ni, nj = i+di[d], j+dj[d]
                    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] > 0:
                        q.append((ni, nj))
                        # print('새로 append 함', q)
                        visited[ni][nj] = 1  # 디큐할 때가 아니라 인큐할 때 방문처리 
    
    return iceburg
# while True:
#     counting()
#     if iceburg >= 2:
#         # print('iceburg 개수 달성으로 종료')
#         print(year)
#         break
#     # 모든 빙하가 녹을 때까지 2개 이상으로 나뉘지 않는 경우 
#     # 모든 빙하가 녹음? -> 
#     elif no_more_search == True:
#         print(0)
#         break

iceburg = counting()
# print(year)
# print(iceburg)

if iceburg >= 2:
    print(year)
else:
    print(0)

# print('원래 arr')
# pprint(arr)

# print('원래 surroundedby')
# pprint(surroundedby)

# finding(arr, surroundedby)
# print('fiding 다음 surroundedby')
# pprint(surroundedby)

# melting(arr, surroundedby)
# print('melting 다음 arr')
# pprint(arr)