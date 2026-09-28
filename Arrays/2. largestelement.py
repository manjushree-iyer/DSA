n = int(input())
arr = list(map(int, input().split()))

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)


# Time Complexity : O(n) -> only one for loop 
# Space Complexity : O(1) -> no new data structures are created even if the inpute size increases. 