n = int(input())
arr = list(map(int, input().split()))

even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)

# Time Complexity : O(n) -> We visit every element once.

# Space Complexity : Space = O(1) -> We only maintain two extra variables: even and odd.