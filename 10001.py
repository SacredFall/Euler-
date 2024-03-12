#10001st prime

def primechecking():  
    for i in factors:
        c=0
        for j in range(1,i):
            if i%j==0:
                c += 1
        if c==1:
            primefactors.append(i)