def gcd(a, b):
    s, r = 0, b
    old_s, old_r = 1, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    if b != 0:
        bezu = (old_r - old_s * a) // b
    else:
        bezu = 0
    return (old_r, old_s, bezu)


a, b = map(int, input().split())
print(gcd(a, b))
