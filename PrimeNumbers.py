#<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
#<p>What is the largest prime factor of the number $600851475143$?</p>

factors = []
primefactors = []
def factorchecking(x):
    for i in range(1,x+1):
        if x%i == 0:
            factors.append(i)

def primechecking():  
    for i in factors:
        c=0
        for j in range(1,i):
            if i%j==0:
                c += 1
        if c==1:
            primefactors.append(i)

factorchecking(52)
primechecking()
print(primefactors)



