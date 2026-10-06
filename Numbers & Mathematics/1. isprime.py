n = int(input())

if n < 2:
    print("Not Prime")
else:
    flag = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = False
            break

    print("Prime" if flag else "Not Prime")

# Time Complexity : O(root n) -> we are checking for root n numbers
# Space Complexity : O(1) -> no new data structures created