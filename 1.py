#https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true

#If we list all the natural numbers below  that are multiples of 3 or 5 , we get 3,5,6,9. The sum of these multiples is 23 .

#Find the sum of all the multiples of 3 or 5 below N.

multiple = []
testcase = input('How much test cases: ')
N = int(input("Your Number: "))
sum = 0

for i in range(1,N):
    if i%3 == 0:
        multiple.append(int(i))
    elif i%5 == 0:
        multiple.append(int(i))

for i in range(0,len(multiple)):
    sum += multiple[i]

print(sum)
    




