# 2439. 별 찍기 - 2

N = int(input())
for n in range(1, N+1):
    ans = '*' * n
    print(f'{ans:>{N}}')  # 전체 자리수는 N개 