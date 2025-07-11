def fun(text):
    stack = []
    for i in text:
        stack.append(i)
    rever = ''
    while stack:
        rever += stack.pop()
    return rever

print(fun('deloitte'))
























