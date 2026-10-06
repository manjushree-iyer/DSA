🧵 STRINGS 
1. First ask: WHAT is the question asking?
If question says...	Immediately think...
Reverse string	Traverse backwards / [::-1]
Palindrome	Two pointers
Count vowels/consonants	Traverse + counter
Frequency of characters	Dictionary / Counter
First non-repeating	Frequency map → scan again
Anagram	Frequency / Counter
Remove duplicates	Set
Toggle case	.upper() / .lower()
Count words	.split()
Longest word	split() + running maximum
Reverse words	split() → reverse() → join()
String compression	Consecutive counting
Most/least frequent	Counter + max() / min()
Remove vowels	Filtering
String rotation	s2 in s1+s1
Longest substring	Sliding Window
Valid parentheses/brackets	Stack
Longest common prefix	Start with prefix → keep shrinking


2. 🔑 Your STRING toolbox
dict / Counter → "HOW MANY?"
from collections import Counterfreq = Counter(s)


Example:
banana → {'a':3, 'n':2, 'b':1}

Use for:
- frequency
- anagram
- most frequent
- least frequent
- first non-repeating
set → "HAVE I SEEN THIS?"
seen = set()if ch not in seen:    seen.add(ch)


Use for:
- remove duplicates
- detecting repeated characters
- longest substring without repeating
counter variable → "HOW MANY SATISFY A CONDITION?"
count = 0for ch in s:    if condition:        count += 1


Use for:
- vowels
- consonants
- digits
- spaces
- etc.
3. 🔥 The most important string operations
s[::-1]             # reverses.lower()           # lowercases.upper()           # uppercases.swapcase()        # toggle cases.split()           # string → list of words" ".join(words)     # list → strings.startswith(x)     # starts with x?s.endswith(x)       # ends with x?ch.isalpha()        # alphabet?ch.isdigit()        # digit?ch.isupper()        # uppercase?ch.islower()        # lowercase?len(s)              # length


Remember:
split()  → breaks
join()   → combines

4. 🧠 The BIG patterns
Pattern 1 — Simple Traversal
Question involves examining every character:
for ch in s:    ...


Usually:
O(n) time
Examples:
- count vowels
- toggle case
- remove vowels
- frequency
Pattern 2 — Two Pointers
Question involves both ends:
left = 0right = len(s)-1while left < right:    ...    left += 1    right -= 1


Think:
Compare / move inward

Use for:
- palindrome
- reverse-related problems
Usually:
O(n) time, O(1) extra space
Pattern 3 — Frequency Map
Question asks:
"How many times does each character occur?"

from collections import Counterfreq = Counter(s)


Think:
Character → Count

Usually:
O(n) time, O(n) space
Pattern 4 — Set
Question asks:
"Have I already seen this?"

seen = set()if ch in seen:    ...else:    seen.add(ch)


Think:
Seen / Not Seen

Pattern 5 — Filtering
Question says:
Remove / keep only certain characters.

result = ""for ch in s:    if condition:        result += ch


Examples:
Remove vowels
Keep digits
Remove spaces
Keep alphabets

Think:
Traverse → condition → keep

Pattern 6 — Running Maximum/Minimum
Question asks:
Longest / shortest / maximum / minimum?

Maintain an answer while scanning.
maximum = 0for x in something:    maximum = max(maximum, value)


Examples:
- longest word
- most frequent
- longest prefix
- maximum length
5. 🚨 Sliding Window
This is VERY important.
Whenever you see:
longest/shortest substring

or
continuous section

think:
SLIDING WINDOW
Basic structure:
left = 0for right in range(len(s)):    # add right character    # if window becomes invalid:    # move left    # update answer


Example:
Longest substring without repeating
abcabcbb

Use:
left  → shrinks window
right → expands window
set/dict → remembers characters

Think:
Expand → violation → shrink → continue

Usually:
O(n)
6. 🥇 Stack
If you see:
- parentheses
- brackets
- nested brackets
- matching opening/closing symbols
Immediately think:
STACK
stack = []# openingstack.append(ch)# closingstack.pop()


Remember:
Last opened → first closed

Example:
{ [ ( ) ] }
      ↑
      ↓
   closes first

7. 🧩 Longest Common Prefix
Think:
Start big → keep shrinking

prefix = words[0]for word in words[1:]:    while not word.startswith(prefix):        prefix = prefix[:-1]


Example:
flower
flow
flight

flower
  ↓
flow
  ↓
flo
  ↓
fl

Answer:
fl

8. 🔄 String Rotation
Very useful shortcut:
if len(s1) == len(s2) and s2 in s1 + s1:    print("YES")


Remember:
Rotation → double the original string

abcd + abcd
= abcdabcd

Every rotation appears inside it.
9. ⚡ Complexity Cheat Sheet
Pattern	Time	Extra Space
Simple traversal	O(n)	O(1)
Two pointers	O(n)	O(1)
Frequency dictionary	O(n)	O(n)
Set	O(n)	O(n)
Sliding window	O(n)	O(n)
Stack	O(n)	O(n)
split()	O(n)	O(n)
Sorting string	O(n log n)	O(n)


Golden rule:
One loop → usually O(n)
Two nested loops → usually O(n²)
Dictionary/set → usually O(n) time + O(n) space
Sorting → O(n log n)
🧠 THE 30-SECOND STRING DECISION TREE
When you see a new string question, ask:
                    STRING
                      │
          ┌───────────┴───────────┐
          ↓                       ↓
     Just examine?            Special structure?
          │                       │
       LOOP                 ┌─────┼──────────┐
                            ↓     ↓          ↓
                         Ends?  Frequency?  Continuous?
                           │       │          │
                     Two pointers Dict     Sliding
                           │       │        Window
                      Palindrome  Anagram   Longest/
                      Reverse     Frequency  Shortest

And:
Brackets?       → STACK
Seen before?    → SET
How many?       → DICT / COUNTER
Longest?        → RUNNING MAX / SLIDING WINDOW
Starts with?    → startswith()
Words?          → split()
Rotation?       → s+s

🔥 FINAL MEMORY TRICK
Before the exam, literally remember these 8 words:
LOOP — TWO POINTERS — DICT — SET — FILTER — STACK — WINDOW — SPLIT

Almost every beginner/intermediate string problem you're likely to encounter can be recognized through one of these patterns.
And don't memorize 20 codes. Recognize the pattern → choose the data structure → write the basic template → dry-run.
That's how you'll be able to solve a new string question you've never seen before, instead of only reproducing the questions you've practiced.