#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with and , the first terms will be:
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

testcases = int(input())
tests = []


for i in range (testcases):
    x = input('')  #amount of test cases
    tests.append(i)

def Fibonacci():
    term1 = 0
    term2 = 1
    next_term = term2
    x = 0
    N = 10 #n'th term
    global Sequence
    Sequence =[]
    while x <= (N):
        x += 1
        Sequence.append(next_term)
        term1 = term2
        term2 = next_term
        next_term = term1 + term2

Fibonacci()
print(Sequence)

    
         
 