n = int(input())
blocks = [
    int(input())
    for _ in range(n)
]

each_block = sum(blocks) // n

ans = 0
for block in blocks:
    if block > each_block:
        ans += (block - each_block)

print(ans)
