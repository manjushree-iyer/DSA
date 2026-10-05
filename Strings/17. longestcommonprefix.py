n = int(input())

words = []

for _ in range(n):
    words.append(input())

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)

# Time Complexity : O(n × m) -> Because in the worst case, we may inspect up to m characters across n words.
# Space Complexity : O(n × m) -> The prefix variable itself only needs up to O(m) space, but the words list dominates because we're storing all the input strings.