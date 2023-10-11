# 1991. 트리 순회

# 1. 트리의 정보를 딕셔너리로 받기
N = int(input())  # N: 노드의 개수
data = {}  # 트리의 정보를 담을 빈 딕셔너리 선언
for _ in range(N):
    root, left, right = input().split()
    data[root] = left, right

# 2. 전위순회 (부모 -> 좌 -> 우)
def preorder(v):  # v: 현재 탐색중인 노드
    if v != '.':
        print(v, end='')      # 현재 노드 기록
        preorder(data[v][0])  # 왼쪽 노드 탐색
        preorder(data[v][1])  # 오른쪽 노드 탐색

# 3. 중위순회 (좌 -> 부모 -> 우)
def inorder(v):
    if v != '.':
        inorder(data[v][0])   # 왼쪽 노드 탐색
        print(v, end='')      # 현재 노드 기록
        inorder(data[v][1])   # 오른쪽 노드 탐색

# 4. 후위순회 (좌 -> 우 -> 부모)
def postorder(v):
    if v != '.':
        postorder(data[v][0])  # 왼쪽 노드 탐색
        postorder(data[v][1])  # 오른쪽 노드 탐색
        print(v, end='')       # 현재 노드 기록

# 5. 결과 출력하기
preorder('A')
print('')
inorder('A')
print('')
postorder('A')