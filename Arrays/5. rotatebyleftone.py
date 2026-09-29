n = int(input())
arr = list(map(int, input().split()))

first = arr[0]

for i in range(n - 1):
    arr[i] = arr[i + 1]

arr[n - 1] = first

print(*arr)

# Time Complexity : O(n) -> We shift almost every element once.
# Space Complexity :  O(1) -> We're modifying the same array and use only one new variable