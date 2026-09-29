n = int(input())
arr = list(map(int, input().split()))

last = arr[-1]

for i in range(n-1, 0, -1):
    arr[i] = arr[i - 1]

arr[0] = last 

print(*arr)

# Time Complexity : O(n) -> We shift almost every element once.
# Space Complexity :  O(1) -> We're modifying the same array and use only one new variable