#Find the largest palindrome made from the product of two 3-digit numbers.
stuff = []
for i in range (100,999):
    for j in range(100,999):
        if str(i*j) == str(i*j)[::-1]:
            stuff.append(int(i*j))

print(max(stuff))