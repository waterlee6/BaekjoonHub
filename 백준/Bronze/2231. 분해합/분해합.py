N = int(input())  # N: 주어진 분해합
ans = 0  # 가장 작은 생성자를 담을 변수, 조건에 걸리지 않을 경우 그대로 0을 출력

# 분해합(N)을 받아서 생성자(M)를 구하는 함수
# 분해합 N을 받았을 때, 그 생성자는 반드시 N보다 작아야 함
def f(N):
    global ans

    for num in range(1, N+1):
        # num의 분해합은 num 자기자신에 각 자리수의 합을 더한 것
        # ★★★ int를 str으로 변환해서 map 함수를 사용해 바로 int로 변환 -> map 그대로 sum 가능함
        dsum = num + sum(map(int, str(num)))
        if dsum == N:  # num의 분해합이 N과 같으면
            ans = num  # 그 때의 num이 최소 생성자
            return     # 바로 return

f(N)
print(ans)