s1 = input()
s2 = input()

if len(s1) == len(s2) and s2 in s1 + s1:
    print("YES")
else:
    print("NO")

# Time Complexity : O(n) -> Traverse through both the strings and ythen s1 + s1
# Space Complexity :  O(1) -> no new data structure created