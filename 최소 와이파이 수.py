n, m = tuple(map(int, input().split()))
arr = tuple(map(int, input().split()))

ans = 0
start = 0

while start < n:

    if arr[start] == 1:
        ans += 1
        start += (2 * m + 1)
    else:    
        start += 1 

print(ans)