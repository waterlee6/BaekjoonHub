N = int(input())
arr = list(map(int, input().split()))

arr_set = set(arr)


sum_val = 0
result = {}
for i in sorted(arr_set):
    result[i] = sum_val
    sum_val += 1


for i in range(N):
    print(result[arr[i]], end=' ')
print()
