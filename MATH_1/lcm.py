from sys import stdin

t = int(input())

for i in range(t):
    a, b = map(int,stdin.readline().split())
    a_gcd = a
    b_gcd = b
    while b_gcd!=0:
        gcd = a_gcd%b_gcd
        a_gcd = b_gcd
        b_gcd = gcd
    lcm = (a*b)/a_gcd
    print("{:.0f}".format(lcm))