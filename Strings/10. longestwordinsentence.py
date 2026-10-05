sentence = input()

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> The split() function creates a new list so the space complexity is O(n)