# 25304. 영수증

# import sys
# sys.stdin = open('input.txt')
X = int(input())  # X: 총 금액
N = int(input())  # N: 물건의 종류
item = []  # 가격, 개수
for _ in range(N):
    item.extend(list(map(int, input().split())))
# print(item)

total = 0  # 물건의 총 금액 계산
for n in range(N):  # n: 0, 1, 2, 3
    total += item[n*2] * item[n*2+1]

if X == total:
    print('Yes')
else:
    print('No')
