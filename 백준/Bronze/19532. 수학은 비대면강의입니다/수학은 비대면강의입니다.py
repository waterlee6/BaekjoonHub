# 19532. 수학은 비대면강의입니다

# import sys
# sys.stdin = open('input.txt')
a, b, c, d, e, f = map(int, input().split())

# 연립방정식 풀이로 풀어도 되지만 2000개 밖에 안되므로 brute force 돌려서 풀기
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            ans = (x, y)

print(*ans)