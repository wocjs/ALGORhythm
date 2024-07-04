a = int(input())
b = int(input())
c = int(input())
nm = a*b*c
nm = str(nm)
arr = [0]*10

for char in nm:
    arr[int(char)]+=1
for i in arr:
    print(i)