arr = str(input())
le = len(arr)


def find(word, l):
    if l == 1:
        return True
    w1 = word[:l // 2]
    w2 = word[l // 2 + 1]
    if word != word[::-1]:
        return False
    if find(w1, len(w1)) and find(w2, len(w2)):
        return True


if find(arr, le):
    print("AKARAKA")
else:
    print("IPSELENTI")
