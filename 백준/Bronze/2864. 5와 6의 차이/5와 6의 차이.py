
a, b = map(str, input().split())
mxa, mxb = '', ''
for c in a:
    if c == '5':
        mxa += '6'
    else:
        mxa += c
for c in b:
    if c == '5':
        mxb += '6'
    else:
        mxb += c
mna, mnb = '', ''
for c in a:
    if c == '6':
        mna += '5'
    else:
        mna += c
for c in b:
    if c == '6':
        mnb += '5'
    else:
        mnb += c
mx = int(mxa) + int(mxb)
mn = int(mna) + int(mnb)

print(mn, mx)