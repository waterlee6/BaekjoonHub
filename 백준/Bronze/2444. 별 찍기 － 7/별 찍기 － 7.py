# 2444. 별 찍기 - 7

# N = int(input())
# for n in range(N):  # n: 0, 1, 2, 3, 4
#     ans = '*' * (2*n + 1)
#     print(f'{ans:^{2*(N-1)+1}}')
# for n in range(N-2, -1, -1):  # n: 3, 2, 1, 0
#     ans = '*' * (2*n + 1)
#     print(f'{ans:^{2*(N-1)+1}}')


# print 두 개 말고 하나로 나와야 하나?
N = int(input())

# 각 행별 별의 개수 입력을 위한 리스트
stars = []
for n in range(N):  # n: 0, 1, 2, 3, 4
    stars.append(2*n + 1)
for n in range(N-2, -1, -1):  # n: 3, 2, 1, 0
    stars.append(2*n + 1)
# print(stars)

# 각 행별 공백 입력을 위한 리스트
blank = []
for b in range(N-1, -1, -1):
    blank.append(b)
for b in range(1, N):
    blank.append(b)
# print(blank)

for i in range(2*N - 1):
    ans = ' '*blank[i] + '*' * stars[i]
    # print(f'{ans:^{2*(N-1)+1}}')  # 가운데정렬 말고 우측정렬로 해야 하나??
    print(ans)