def prime(x):
    if x<=1:
        print("Enter a bigger number")
    else:
        n=[]
        for i in range(1, x+1):
            if x%i==0:
                n.append(i)

        if len(n)==2:
            print("Prime")
        else:
            print("Composite")

prime(x=int(input()))


