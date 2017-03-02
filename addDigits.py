sum=0
num=1234
while num>0:
    sum=sum+(num%10)
    num=int(num/10)
print(sum)