# 4803. 트리

'''
트리가 아닌 것?
- 순회하는 것

인풋받기
- 여러개의 테스트 케이스?

트리의 개수를 세기
- 일단 그래프를 그려야 하니까 인접 행렬을 만들어보자

- 트리의 개수라는게 뭐지?
- 순회하지 않고 연결되어 있는 그래프
- 하나의 정점만 있어도 트리
'''


def bfs(i, arr):  # i: 현재 탐색중인 정점, arr: 인접행렬
    global Tree, visited

    # 1. Q, 시작점 인큐
    Q = []
    Q.append(i)

    # 2. BFS 탐색
    while Q:  # Q가 남아있는 동안

        # 2-1. 디큐하기(탐색하기) + visited하기
        '''
        
        '''
        i = Q.pop(0)
        if visited[i] == 0:
            visited[i] = 1  # ★디큐할 때 visited
        else:
            Tree = False
            # break  # visited에 이미 표시되어 있으면 순회이므로 Tree를 체크하고 while문 break

        # 2-2. 인큐하기
        for j in range(1, n + 1):
            if arr[i][j] == 1 and visited[j] == 0:  # i와 j 노드가 연결되어 있고, j노드를 방문 전이면
                Q.append(j)

    # 3. while문을 다 돌고 나올때까지 Tree가 True이면 트리라는 것이므로
    # if Tree == True:
    #     T += 1




tc = 0  # 테스트 케이스의 번호를 셀 변수
while True:
    n, m = map(int, input().split())  # n: 정점의 개수, m: 간선의 개수
    tc += 1

    T = 0  # 트리의 개수를 셀 변수

    if n == 0 and m == 0:
        break  # while문 탈출
    else:
        # 인접행렬 만들기
        arr = [[0] * (n + 1) for _ in range(n + 1)]  # 인접행렬을 기록할 빈 행렬
        for _ in range(m):
            v1, v2 = map(int, input().split())
            arr[v1][v2] = 1
            arr[v2][v1] = 1
        # pprint(arr)
        # print(n, m)

        # visited 만들기
        visited = [0] * (n + 1)

        # [BFS로 탐색하기]
        # 시작노드 i를 뭘로 설정? -> visited[i]가 아직 미탐색이면
        for i in range(1, n + 1):
            Tree = True  # 순회인지 아닌지를 판단할 변수(매 tc마다 초기화)
            if visited[i] == 0:
                bfs(i, arr)
                if Tree:  ######
                    T += 1
                # print(visited)
                # print(Tree)
                # print(T)

        # print(T)
        '''
        여기서 Tree == False 인 걸로 판단하면 False, False, True인 경우 True 개수가 세짐
        '''
        if T == 0:
            print(f'Case {tc}: No trees.')
        elif T == 1:
            print(f'Case {tc}: There is one tree.')
        else:
            print(f'Case {tc}: A forest of {T} trees.')
