import sys
INT_MAX = sys.maxsize


n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = INT_MAX

for i in range(n):
    ans = min(ans, arr[n + i] - arr[i])
print(ans)