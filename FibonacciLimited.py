Sequence =[]
sum = int(0)
def Fibonacci():
    term1 = 0
    term2 = 1
    next_term = term2
    maximumvalue = int(input())
    while term2 < (maximumvalue):
        Sequence.append(next_term)
        term1 = term2
        term2 = next_term
        next_term = term1 + term2

Fibonacci()
Sequence.pop(-1)
print(Sequence)


for i in range(len(Sequence)):
    if Sequence[i]%2 == 0:
        sum += Sequence[i]

    
print(sum)

