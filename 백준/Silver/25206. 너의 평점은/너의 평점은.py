
score = {
    'A+': 4.5,
    'A0': 4,
    'B+': 3.5,
    'B0': 3,
    'C+': 2.5,
    'C0': 2,
    'D+': 1.5,
    'D0': 1,
    'F': 0
}
sm = 0
cnt = 0
for _ in range(20):
    name, h, alpha = map(str, input().split())
    h = int(h[0])

    if score.get(alpha) is None:
        continue
    sm += h * score[alpha]
    cnt += h
print(round(sm / cnt, 6))