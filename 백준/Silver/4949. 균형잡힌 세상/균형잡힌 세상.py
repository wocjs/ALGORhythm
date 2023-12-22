while True:
    letter = input()
    if letter == '.':
        break
    stack = []
    for char in letter:
        if char == '[':
            stack.append('[')
        elif char == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)
                break
        elif char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
                break
    if stack:
        print('no')
        continue
    print('yes')