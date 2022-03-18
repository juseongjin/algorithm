string = input()
res=''
for s in string:
    if 'A' <= s <= 'Z':
        s = ord(s)+13
        if (91 <= s):
            s-=26
        res+=chr(s)
    elif 'a' <= s <= 'z':
        s = ord(s)+13
        if (123 <= s):
            s-=26
        res+=chr(s)
    else:
        res+=s
print(res)