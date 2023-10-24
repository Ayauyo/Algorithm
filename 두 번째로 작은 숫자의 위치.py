n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

second = 0

for i in range(n - 1):
    if sorted_nums[i + 1] > sorted_nums[i]:
        second = sorted_nums[i + 1]
        break

cnt = 0
for i in range(n):
    if nums[i] == second:
        cnt += 1

ans = -1
if cnt == 1:
    ans = (nums.index(second) + 1)

print(ans)