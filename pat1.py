num=5
for i in range(num+1):
    print(str(i)*i)

for i in range(1,num+1):
    print()
    for j in range(1,i+1):
        print(j,end='')
