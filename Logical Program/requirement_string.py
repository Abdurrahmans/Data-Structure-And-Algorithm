n = 'x3y2z1'
s = ''
for i in n:
    if i.isalpha():
        s += i
        prev = i
    else:
        if i.isdigit():
            s += prev*(int(i)-1)
print(s)
