arr= list(map(int, input().split()))

arr.sort()

a, b = arr[0], arr[1]
sum_abc = max(arr)
c = sum_abc - a - b

print(a, b, c)