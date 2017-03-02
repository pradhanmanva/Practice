num=10
char=65
for i in range(1,num+1):
    print(chr(char)*i)
    char=char+1

for i in range(1,num+1):
    char=65
    print()
    for j in range(1,i+1):
        print(chr(char),end='')
        char=char+1

char=65
for i in range(1,num+1):
    print()
    for j in range(num-i,0,-1):
        print(end=" ")
    for k in range(1,i+1):
        print(chr(char),end='')
        char=char+1


for i in range(1,num+1):
    char = 65
    print()
    for j in range(num-i,0,-1):
        print(end=" ")
    for k in range(1,i+1):
        print(chr(char),end='')
        char=char+1