import math
n = input()
lst = [0]*9
for num in n:
    if int(num) == 9:
        lst[6] += 1
    else:
        lst[int(num)] += 1
lst[6] /= 2
print(math.ceil((max(lst))))
