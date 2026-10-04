n = int(input())
arr = list(map(int, input().split()))

current = arr[0]
maximum = arr[0]

for i in range(1, n):
    current = max(arr[i], current + arr[i])
    maximum = max(maximum, current)

print(maximum)

# Time Complexity : O(n) -> we traverse the array only once

# Space Complexity : O(1) -> we use two variables current and maximum.