sentence = input()

words = sentence.split()

words.reverse()

print(" ".join(words))

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(n) -> The split() function creates a new list so the space complexity is O(n)