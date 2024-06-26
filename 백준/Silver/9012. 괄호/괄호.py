
for tc in range(int(input())):
    s = input()
    st = 0
    for c in s:
        if c == '(':
            st += 1
        else:
            st -= 1
            if st < 0:
                print("NO")
                break
    else:
        if st > 0:
            print("NO")
        else:
            print("YES")