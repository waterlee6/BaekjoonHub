# 2563. 색종이

# 색종이의 좌측 하단 좌표가 주어지는 것 주의

# 색종이가 있는 부분에 표시 -> 몇 겹 겹치는지는 상관 없음
# 아무것도 없는 부분의 넓이 구하기
# 전체 도화지 - 아무것도 없는 부분

# import sys
# sys.stdin = open('input.txt')
N = int(input())  # N: 색종이의 개수
arr = [[2] * 100 for _ in range(100)]  # 흰색 도화지를 미리 만들어 놓고 시작
# print(arr)

# 1. 도화지에서 색종이를 표시하기
for _ in range(N):
    m, n = map(int, input().split())  # m: 왼쪽 변 사이의 거리, n: 아래쪽 변 사이의 거리
    for width in range(10):  # 색종이의 가로 길이 size: 0, 1, 2, ... , 9
        for height in range(10):  # 색종이의 세로 길이
            arr[m + width][90-n + height] = 1  # 색종이가 있는 부분은 1로 표시
            # 행 좌표는 주어진 m값을 그대로 사용
            # 열 좌표는 도화지 크기(100) - 색종이 크기(10) - 주어진 n값 = 90-n 으로 계산


# 2. 색종이의 크기 재기
# 색종이가 있는 부분만 1이므로 1의 개수를 세면 됨
cnt = 0  # 1의 개수(색종이가 있는 부분)를 셀 변수
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)