arr = input().split('-')
nums = []

for i in arr:
    sm = 0
    tmp = i.split('+')
    for j in tmp:
        sm += int(j)
    nums.append(sm)
ans = nums[0]
for i in range(1, len(nums)):
    ans -= int(nums[i])
print(ans)