n = int(input())

total = 1

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        total += i

        if i != n // i:
            total += n // i

print("Perfect" if n > 1 and total == n else "Not Perfect")
