
def chk(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


n = int(input())
for _ in range(n):
    nm = int(input())
    if nm == 0 or nm == 1:
        print(2)
        continue
    while True:
        if chk(nm):
            print(nm)
            break
        nm += 1