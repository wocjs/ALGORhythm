# B1259
while True:
    _str = input()
    if _str == '0':
        break
    if _str == _str[::-1]:
        print('yes')
    else:
        print('no')