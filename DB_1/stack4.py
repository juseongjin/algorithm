n=int(input())
seq=[]
op = []
base = 1
answer = True

for _ in range(n):
    num = int(input())
    while base <= num:
        seq.append(base)
        op.append("+")
        base += 1
    if num == seq[-1]:
        seq.pop()
        op.append("-")
    else:
        answer = False

if answer == True:
    for _ in  op:
        print(_)
else:
    print("NO")