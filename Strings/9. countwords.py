s = input().strip()

if not s:
    print(0)
else:
    print(len(s.split()))

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> The split() function creates a new list so the space complexity is O(n)