import sys
T = int(sys.stdin.readline())

for _ in range(T):
    before = sys.stdin.readline().split()
    word = []
    for y in before:
        word.append(y[::-1])
    print(' '.join(word))