s = input().lower()

vowels = "aeiou"

v = 0
c = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels = ", v)
print("Consonants = ", c)

# Time Complexity : O(n) -> Traverse through the string once
# Space Complexity :  O(1) -> only two new variables created vowels and consonants and not any new data structures
