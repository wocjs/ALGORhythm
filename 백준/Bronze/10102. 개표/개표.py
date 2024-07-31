
score = [0, 0]
n = int(input())
vote = input()
for c in vote:
    if c == 'A':
        score[0] += 1
    else:
        score[1] += 1
if score[0] == score[1]:
    print('Tie')
elif score[0] > score[1]:
    print('A')
else:
    print('B')