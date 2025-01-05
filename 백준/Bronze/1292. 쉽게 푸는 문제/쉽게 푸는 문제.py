a,b=map(int,input().split())
data=[0]
sum=0

for i in range(1,b+1):
  for j in range(i):
    data.append(i)

for i in range(a, b+1):
  sum+=data[i]
print(sum)