n = int(input())
for _ in range(n):
    word = input()
    fr, bk = 0, len(word)-1
    chk = 0

    for _ in range(len(word)):
        if fr > bk:
            break
        if word[fr] == word[bk]:
            fr += 1
            bk -= 1
            continue
        if word[fr] == word[bk-1]:
            tmp = word[fr:bk]
            if tmp == tmp[::-1]:
                chk = 1
                break
        if word[fr+1] == word[bk]:
            tmp = word[fr+1:bk+1]
            if tmp == tmp[::-1]:
                chk = 1
                break

        chk = 2
        break
    print(chk)