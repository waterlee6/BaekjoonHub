# 1436. 영화감독 숌

N = int(input())
key = '666'
n = 0   # 종말의 수를 셀 변수
i = 0   # 반복문을 돌 변수

while n < N:
    i += 1
    if key in str(i):
        n += 1

print(i)
