num = 20
flag = 1
for i in range(2, num):
    flag=1;
    for j in range(2, i):
        if i % j == 0:
            flag = 0
            break;
    if flag == 1:
        print("%d is prime" % i)
    else:
        print("%d is not prime" % i)
