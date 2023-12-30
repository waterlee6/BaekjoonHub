# 18258. 큐 2

import sys
input = sys.stdin.readline
from collections import deque
q = deque()

N = int(input())
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        q.append(int(order[1]))
    elif order[0] == 'pop':
        if q:
            num = q.popleft()
            print(num)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
