#10001st prim


def prime(n):
    if n > 1:

        for i in range(2, int(n/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
        else:
            return True
seen = 0
n = 1
while seen < 10001:
    n += 1
    if prime(n):
        seen += 1

print(n)