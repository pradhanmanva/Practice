num=371/153
dummy=num;
sum=0
while num>0:
    sum=sum+(num%10)**3
    num=int(num/10)
if dummy==sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")