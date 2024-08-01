
dic = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}
sm = 0
_str = input()
for c in _str:
    if c in dic:
        sm += 1
print(sm)