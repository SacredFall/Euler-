
tests = []
testcase = int(input('How much test cases: '))

for i in range(1,testcase+1):
    x = int(input(f'What is your {i} test case?\n > '))
    tests.append(x)

def n(N):
    multiple = []
    sum = 0
    for i in range(1,N):
        if i%3 == 0:
            multiple.append(int(i))
        elif i%5 == 0:
            multiple.append(int(i))
    for i in range(0,len(multiple)):
        sum += multiple[i]

    print(sum)
    

for i in tests:
    n(i)