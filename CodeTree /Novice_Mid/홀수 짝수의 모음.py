n = int(input())
arr = tuple(map(int, input().split()))

odd, even = 0, 0

for i in range(n):
    if arr[i] % 2 == 1:
        odd += 1
    else:
        even += 1    


ans = 0
while True:

    if ans % 2 == 0:

        if even:
            even -= 1
            ans +=1

        elif odd >= 2:
            odd -= 2
            ans += 1

        else:
            
            if odd > 0 or even > 0:
                ans -= 1
            break    

    else:

        if odd:
            odd -= 1
            ans += 1
        
        else:
            break

print(ans)