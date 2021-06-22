n = 'Alex12345Leesa6789'
s1 = s2 = ' '
for i in n:
    if i.isalpha():
        s1 += i
    else:
        if i.isdigit():
            s2 += i
print(s1 + s2)
