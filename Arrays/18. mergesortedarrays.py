n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

i = j = 0
result = []

while i < n and j < m:
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

while i < n:
    result.append(arr1[i])
    i += 1

while j < m:
    result.append(arr2[j])
    j += 1

print(*result)

# Time Complexity : O(n + m) -> Traversing through array1 and array2

# Space Complexity : O(n + m) -> Variable Result contains elements of both arr1 and arr2