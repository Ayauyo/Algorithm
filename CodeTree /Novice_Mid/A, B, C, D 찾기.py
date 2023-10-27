arr = list(map(int, input().split()))
arr.sort()

a, b, c = arr[0], arr[1], arr[2]
sum_abcd = max(arr)
d = sum_abcd - a - b - c

print(a, b, c, d)