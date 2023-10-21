# 2839. 설탕 배달

N = int(input())  # N: 배달할 설탕의 kg
min_bags = 5000   # 최소로 필요한 봉지의 수
bags = 10000      # 봉지의 개수를 셀 변수

for i in range(N):
    for j in range(N):
        if (3 * i) + (5 * j) == N:
             bags = i + j
             if bags < min_bags:
                 min_bags = bags

if bags == 10000:  # 마지막까지 bags가 변경되지 않았다면 답이 없는 것이므로 -1 출력
    min_bags = -1

print(min_bags)