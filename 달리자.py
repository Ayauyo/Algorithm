n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):

    if a[i] > b[i]:
        cnt = a[i] - b[i]
        a[i] -= cnt
        a[i + 1] += cnt
        ans += cnt

print(ans)        