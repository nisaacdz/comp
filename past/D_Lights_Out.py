a, b , c = map(int, input().split())
d, e, f = map(int, input().split())
g, h, i = map(int, input().split())

a2 = a + b + d
b2 = b + a + c + e
c2 = c + b + f
d2 = a + d + e + g
e2 = e + d + f + b + h
f2 = f + c + e + i
g2 = g + h + d
h2 = g + h + e + i
i2 = h + i + f

print(1 - a2 % 2, 1 - b2 % 2, 1 - c2 % 2, sep="")
print(1 - d2 % 2, 1 - e2 % 2, 1 - f2 % 2, sep="")
print(1 - g2 % 2, 1 - h2 % 2, 1 - i2 % 2, sep="")