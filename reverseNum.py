rev = 0
r = 0
num = int(1234)
while num > 0:
    r = num % 10
    rev = rev * 10 + r
    num = int(num / 10)
print(rev)
