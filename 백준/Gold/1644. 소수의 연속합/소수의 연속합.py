# 1644. 소수의 연속합
'''
주어진 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 찾기 (없을 경우 0)
자연수의 범위는 4,000,000 이하
4,000,000 이하 연속된 소수의 리스트 np를 먼저 만들고,
그 np를 대상으로 투 포인터 알고리즘 적용하기

>> 소수 <<
1과 자기 자신만을 약수로 가지는 수
'''
import math
import sys
input = sys.stdin.readline

n = int(input())  # n: 주어진 자연수
pn = []           # n 이하의 소수를 담을 리스트
root = int(math.sqrt(n))

# 1. n 이하의 연속된 소수 리스트 구하기 -> 에라토스테네스의 체 ====================================
'''
하나의 수가 소수인지 아닌지를 판별할 때는 그 수의 제곱근 만큼만 확인하면 됨
예를 들어 20의 제곱근은 대략 4와 5 사이일 것이고, 약수는 1, 2, 4, 5, 10, 20의 6개임
제곱근을 기점으로 양 쪽의 두 수를 곱한 값이 20이 되므로, 제곱근 이전까지만 확인하면 약수를 모두 찾을 수 있음
'''

# 1-1. 처음엔 모든 수가 소수(True)인 것으로 초기화
arr = [True for _ in range(n+1)]

# 1-2. 에라토스테네스의 체 알고리즘 수행
# 2부터 n 제곱근까지의 모든 수를 확인하며
for i in range(2, root+1):
    # i가 아직 남아있으면 (소수이면)
    if arr[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if arr[i]:
        pn.append(i)
# print(pn)
# print(len(pn))


# n 이하의 연속된 소수 리스트 구하기 -> 내가 짜본 코드 (넘 느림) =================================
# num_list = [num for num in range(2, (n+1))]  # 전체 숫자를 담을 리스트
# min_num = 1
#
# while min_num <= root:
#     # 아직 처리하지 않은 가장 작은 수를 찾아 prime_list에 추가
#     min_num = num_list.pop(0)     # num_list에서 제거
#     pn.append(min_num)    # prime_list에 추가
#
#     # 해당 작은 수의 배수를 모두 제거하기
#     for num in num_list:
#         if num % min_num == 0:    # min_num의 배수라면 제거하기
#             num_list.remove(num)
#
# # 남은 수는 다 pn에 넣기 (while문 밖에서!!)
# pn.extend(num_list)
#
# print(pn)
# print(len(pn))


# 2. 반환된 pn 리스트에서 투 포인터 알고리즘 수행
'''
같은 방향으로 진행하는 투 포인터 알고리즘 수행
'''
temp_sum = 0
cnt = 0   # 경우의 수를 셀 변수
end = 0

for start in range(len(pn)):
    # end를 가능한만큼 이동 (temp_sum이 n과 같아지면 start를 이동시켜야 하므로)
    while temp_sum < n and end < len(pn):
        temp_sum += pn[end]
        end += 1

    # end를 다 이동하고 temp_sum 값을 확인
    if temp_sum == n:
        cnt += 1
        
    # start 이동하면 그 값을 빼줌
    temp_sum -= pn[start]

print(cnt)