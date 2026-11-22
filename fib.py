def fib(x):
    if x==0:
        print([])

    elif x==1:
        print([0])

    elif x==2:
        print([0, 1])

    else:
        a,b=0,1
        fib_nums=[a, b]
        for i in range (x-2):
            k=b
            b=a+b
            a=k
            fib_nums.append(b)
        print(fib_nums)


fib(x=int(input()))

#do not enter a negative number