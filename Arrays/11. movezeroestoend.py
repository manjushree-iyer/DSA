n = int(input())
arr = list(map(int, input().split()))

index = 0

for i in range(n):
    if arr[i] != 0:
        arr[index], arr[i] = arr[i], arr[index]
        index += 1

print(*arr)

# Time Complexity : O(n) -> We traverse the array only once

# Space Complexity : Space = O(1) -> We don't create another data structure. we maintain the same array.