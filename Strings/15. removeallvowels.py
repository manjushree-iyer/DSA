s = input()

vowels = "aeiouAEIOU"

result = ""

for ch in s:
    if ch not in vowels:
        result += ch

print(result)

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> We create result, which can contain up to all n characters if there are no vowels: