from sys import stdin
while True:
    up, lo, num, nu = 0, 0, 0, 0
    string = list(stdin.readline().rstrip('\n'))
    
    if not string:
        break
    for s in string:
        if 'A'<= s <= 'Z':
            up+=1
        elif 'a' <= s <= 'z':
            lo+=1
        elif '0' <= s <= '9':
            num+=1
        elif s == ' ':
            nu +=1
    print(lo, up, num, nu)