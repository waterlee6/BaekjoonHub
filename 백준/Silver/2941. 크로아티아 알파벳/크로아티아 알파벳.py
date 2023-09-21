# 2941. 크로아티아 알파벳
# 패턴 매칭으로 풀기?

old_T = input()  # T: target
N = len(old_T)   # N: target의 길이
howmany = 0  # 크로아티아 알파벳의 개수를 셀 변수
howlong = 0  # 크로아티아 알파벳의 총 길이를 셀 변수

# 'dz='와 'z='를 분리해야 하므로 -> 'dz='가 있는 경우에는 아예 바꿔버리고 시작
T = old_T.replace('dz=', 'dz+')
# print(T)

# P의 길이가 3인 경우 탐색('dz+')
howmany += T.count('dz+')
howlong += 3 * howmany

# P의 길이가 2인 경우 탐색
P_list_2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']  # 길이가 2인 P들의 집합
for P in P_list_2:
    M = len(P)  # M = 2
    for i in range(N-M+1):  # T의 범위
        check = 0

        for j in range(M):  # P의 범위
            if T[i+j] == P[j]:
                check += 1

        if check == M:  # j를 돌고 나왔을 때 check가 M이면 타겟을 찾았다는 것이므로
            howmany += 1
            howlong += check


# print(cnt)
ans = N - howlong + howmany
print(ans)

