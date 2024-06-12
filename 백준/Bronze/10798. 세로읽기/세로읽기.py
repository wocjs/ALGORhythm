arr = []
while True:
    try:
        _str = input()
        arr.append(_str)
    except:
        break
for j in range(15):
    for i in range(len(arr)):
        try:
            print(arr[i][j], end='')
        except:
            continue