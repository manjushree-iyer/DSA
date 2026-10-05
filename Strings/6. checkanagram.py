s1 = input()
s2 = input()

if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")

# Time Complexity : O(n log n) -> sorting takes O(nlogn)
# Space Complexity : O(n) -> approximately for the sorted representations.