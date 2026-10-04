arr = list(map(int, input().split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1

    else:
        freq[num] = 1

for key in freq:
    print(key, ":", freq[key])

# Time Complexity : O(n) -> Two different for loops that iterate only once. 
# Remember TC will be O(n^2) only if both the for loops are nested

# Space Complexity : O(n) -> creating a new dictionary freq and its size increases wrt the input