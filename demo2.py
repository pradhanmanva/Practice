import random

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
print ("False")


list = [2,3,4,5,6,7,8,9]
print(list[::2])
random.shuffle(list)
print(list)

print(random.randint(0,4))
print(random.randint(-5,4))
print(random.random())

print(hex(30))
print(oct(30))
print(ord('A'))
print(chr(65))
print(bin(20))

print(2 in list)
print(10 not in list)

print(id(list))

if(3>4 and 6<7):
    print("true")
else:
    print("boo")

print(len(list))

it = iter(list)
for i in it:
    print(i,end=" ")

for i in range(3):
    print('\a')

o="HWLLOEPYTHONG"
print(o.capitalize())