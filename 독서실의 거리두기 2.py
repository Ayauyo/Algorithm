import sys

INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input()))

longest_1 = 0
start_idx_1, finish_idx_1 = -1, -1

for i in range(n):
    if arr[i] == 1:
        for j in range(i + 1, n):
            if arr[j] == 1:
                if j - i > longest_1:
                    longest_1 = j - i
                    start_idx_1 = i
                    finish_idx_1 = j
                break

longest_2 = -1
max_idx = -1

if arr[0] == 0:
    dist = 0
    for i in range(1, n):
        if arr[i] == 1:
            break
        dist += 1    
            
    if dist > longest_2:
            longest_2 = dist
            max_idx = 0
  

if arr[n - 1] == 0:
    dist = 0
    for i in range(n - 2, -1, -1):
        if arr[i] == 1:
            break
        dist += 1    
    if dist > longest_2:
            longest_2 = dist
            max_idx = n - 1


if longest_2 >= longest_1 // 2:
    arr[max_idx] = 1
else:
    arr[(finish_idx_1 + start_idx_1) // 2] = 1

ans = INT_MAX
for i in range(n):
    if arr[i] == 1:
        for j in range(i + 1, n):
            if arr[j] == 1:
                ans = min(ans, j - i)
                break
print(ans)