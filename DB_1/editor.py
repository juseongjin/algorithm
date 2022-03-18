import sys

base = list(sys.stdin.readline().strip())
print(base)
base2 = []
m = int(input())

for _ in range(m):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "L" :
        if base: base2.append(base.pop())
    elif cmd[0] == "D" :
        if base2: base.append(base2.pop())
    elif cmd[0] == "B" :
        if base: base.pop()
    elif cmd[0] == "P" :
        base.append(cmd[1])
print(''.join(base+list(reversed(base2))))