from sys import stdin

str = list(stdin.readline().strip())
reverse=[]
res=[]
i=0

while i <len(str):
    if str[i] == '<':
        res.append(str.pop(i))
        while str[i] != '>':
            res.append(str.pop(i))
    elif str[i] == '>':
        res.append(str.pop(i))
    elif str[i] == ' ':
        res.append(str.pop(i))
    else:
        while len(str)!=0 and str[i] != '<' and str[i] !=' ':       
            reverse.append(str.pop(i))
        for _ in range(len(reverse)):
            res.append(reverse.pop())
print(''.join(res))