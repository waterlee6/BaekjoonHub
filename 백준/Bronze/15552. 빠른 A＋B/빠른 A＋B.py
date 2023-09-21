# 15552. 빠른 A+B

import sys
# input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)