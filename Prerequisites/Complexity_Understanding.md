# DSA Algorithm Complexity Cheat Sheet

| Category                | Algorithm / Operation                |              Time |     Space |
| ----------------------- | ------------------------------------ | ----------------: | --------: |
| **Searching**           | Linear Search                        |              O(n) |      O(1) |
|                         | Binary Search                        |          O(log n) |      O(1) |
| **Sorting**             | Bubble Sort                          |             O(n²) |      O(1) |
|                         | Selection Sort                       |             O(n²) |      O(1) |
|                         | Insertion Sort                       |             O(n²) |      O(1) |
|                         | Merge Sort                           |        O(n log n) |      O(n) |
|                         | Quick Sort                           |             O(n²) | O(log n)* |
|                         | Heap Sort                            |        O(n log n) |      O(1) |
|                         | Counting Sort                        |          O(n + k) |      O(k) |
|                         | Radix Sort                           |             O(nk) |  O(n + k) |
| **Arrays / Strings**    | Traversal                            |              O(n) |      O(1) |
|                         | Two Pointers                         |              O(n) |      O(1) |
|                         | Sliding Window                       |              O(n) |      O(1) |
|                         | Prefix Sum                           |              O(n) |      O(n) |
|                         | Frequency Counting                   |              O(n) |      O(n) |
|                         | Hash Map Lookup                      |      O(1) average |      O(n) |
|                         | Kadane's Algorithm                   |              O(n) |      O(1) |
| **Linked List**         | Access / Search                      |              O(n) |      O(1) |
|                         | Insert at Head                       |              O(1) |      O(1) |
|                         | Delete at Head                       |              O(1) |      O(1) |
|                         | Insert After Known Node              |              O(1) |      O(1) |
|                         | Reverse Linked List                  |              O(n) |      O(1) |
| **Stack**               | Push / Pop / Peek                    |              O(1) |      O(1) |
|                         | Search                               |              O(n) |      O(1) |
| **Queue**               | Enqueue / Dequeue / Peek             |              O(1) |      O(1) |
|                         | Search                               |              O(n) |      O(1) |
| **Binary Tree**         | DFS / Inorder / Preorder / Postorder |              O(n) |      O(h) |
|                         | BFS                                  |              O(n) |      O(n) |
| **BST**                 | Search / Insert / Delete             |              O(n) |      O(h) |
| **Graphs**              | BFS                                  |          O(V + E) |      O(V) |
|                         | DFS                                  |          O(V + E) |      O(V) |
|                         | Dijkstra                             | O((V + E) log V)* |  O(V + E) |
|                         | Bellman-Ford                         |             O(VE) |      O(V) |
|                         | Floyd-Warshall                       |             O(V³) |     O(V²) |
|                         | Topological Sort                     |          O(V + E) |      O(V) |
|                         | Kruskal                              |        O(E log E) |  O(V + E) |
|                         | Prim                                 |       O(E log V)* |  O(V + E) |
| **Dynamic Programming** | Fibonacci DP                         |              O(n) |      O(n) |
|                         | 0/1 Knapsack                         |             O(nW) |     O(nW) |
|                         | Longest Common Subsequence           |             O(mn) |     O(mn) |
|                         | Longest Increasing Subsequence       |             O(n²) |      O(n) |
|                         | Coin Change                          |     O(n × amount) | O(amount) |
| **Recursion**           | Factorial                            |              O(n) |      O(n) |
|                         | Naive Fibonacci                      |             O(2ⁿ) |      O(n) |
| **Backtracking**        | Subsets                              |             O(2ⁿ) |      O(n) |
|                         | Permutations                         |         O(n × n!) |      O(n) |
|                         | N-Queens                             |     O(n!) approx. |      O(n) |

### Complexity Hierarchy — Fast → Slow

**O(1) → O(log n) → O(n) → O(n log n) → O(n²) → O(n³) → O(2ⁿ) → O(n!)**

### Quick Rules

| Pattern                | Complexity |
| ---------------------- | ---------: |
| Direct operation       |       O(1) |
| One loop               |       O(n) |
| Separate loops         |       O(n) |
| Nested loops           |      O(n²) |
| 3 nested loops         |      O(n³) |
| Divide by 2 repeatedly |   O(log n) |
| Efficient sorting      | O(n log n) |
| All subsets            |      O(2ⁿ) |
| All permutations       |      O(n!) |

**n** = number of elements | **V** = vertices | **E** = edges | **h** = tree height | **k** = range/parameter