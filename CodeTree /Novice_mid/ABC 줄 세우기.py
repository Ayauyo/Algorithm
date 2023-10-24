n = int(input())
people = list(input().split())

cnt = 0

while True:

    ans = True

    for i in range(n - 1):
        if ord(people[i]) > ord(people[i + 1]):
            ans = False
            break

    if ans:
        break

    for i in range(n - 1):
        if ord(people[i]) > ord(people[i + 1]):
            temp = people[i]
            people[i] = people[i + 1]
            people[i + 1] = temp
            cnt += 1
            
print(cnt)       
