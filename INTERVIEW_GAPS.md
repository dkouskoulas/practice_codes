# Algorithm Interview Gaps & Priorities

## Coverage Assessment: ~60-70% Complete

### ✅ Strong Coverage (Already Implemented)

**Arrays & Strings:**
- Kadane's algorithm (max/min subarray)
- Prefix sums (1D and 2D)
- Sliding window (fixed and variable size)
- Two pointers (palindrome, remove duplicates, sorted two-sum)

**Sorting:**
- Quick sort, merge sort, heap sort
- Binary search (standard + rotated array variants)

**Hash Maps/Dictionaries:**
- Two sum, group anagrams, frequency counting
- Common interview patterns

**Linked Lists:**
- Reverse, cycle detection (Floyd's)
- Merge two sorted lists
- Find middle node
- Remove nth from end

**Recursion:**
- Factorial, Fibonacci, GCD
- Permutations, Tower of Hanoi
- Power, array sum, reverse string

**Greedy Algorithms:**
- Activity selection
- Fractional knapsack
- Stock profit problems

**Dynamic Programming:**
- 0/1 Knapsack

**Graphs:**
- Topological sort (Kahn's algorithm)

---

## ❌ Major Gaps

### 1. **Trees** (Critical - Very Common in Interviews)

**Missing:**
- Binary tree traversals (inorder, preorder, postorder - both recursive and iterative)
- Level-order traversal (BFS on trees)
- Binary search tree operations (insert, search, delete)
- Lowest common ancestor (LCA)
- Validate BST
- Max depth / height
- Symmetric tree
- Path sum problems
- Invert binary tree

**Priority:** **HIGH** - Trees appear in 30-40% of coding interviews

---

### 2. **Graph Algorithms** (Partial Coverage)

**Missing:**
- BFS traversal (adjacency list)
- DFS traversal (recursive + iterative)
- Shortest path (Dijkstra, BFS for unweighted)
- Connected components
- Course schedule (cycle detection in directed graphs)
- Number of islands
- Clone graph
- Union-Find / Disjoint Set Union

**Have:** Topological sort only

**Priority:** **HIGH**

---

### 3. **Stacks & Queues** (Missing Entirely)

**Missing:**
- Valid parentheses (stack)
- Next greater element (monotonic stack)
- Min stack (O(1) get min)
- Implement queue using stacks
- Evaluate reverse Polish notation
- Daily temperatures

**Priority:** **HIGH** - Stack problems are common warm-ups

---

### 4. **Heaps** (Partial Coverage)

**Have:** Heap sort, K closest points to origin

**Missing:**
- Kth largest element (quickselect or heap)
- Top K frequent elements
- Merge K sorted lists
- Find median from data stream
- Task scheduler

**Priority:** **MEDIUM**

---

### 5. **String Algorithms** (Minimal)

**Have:** Basic palindrome, anagrams

**Missing:**
- Longest common subsequence (LCS)
- Longest common substring
- Longest palindromic substring
- String to integer (atoi)
- Minimum window substring
- Valid palindrome (alphanumeric)

**Priority:** **MEDIUM**

---

### 6. **Dynamic Programming** (Light Coverage)

**Have:** 0/1 Knapsack

**Missing:**
- Longest increasing subsequence (LIS)
- Coin change
- Edit distance
- House robber
- Climbing stairs (DP version, not just recursive)
- Word break
- Unique paths

**Priority:** **MEDIUM-HIGH**

---

### 7. **Backtracking** (Missing Entirely)

**Missing:**
- Subsets / Power set
- Combinations / Combination sum
- Permutations (iterative backtracking version)
- N-Queens
- Word search in grid
- Generate parentheses
- Palindrome partitioning

**Priority:** **MEDIUM**

---

### 8. **Bit Manipulation** (Missing)

**Missing:**
- Single number (XOR tricks)
- Number of 1 bits
- Reverse bits
- Power of two
- Missing number

**Priority:** **LOW-MEDIUM** - Good to know but less common

---

## 🎯 Immediate Action Plan

### Phase 1: Critical Gaps (Add Next)

1. **Binary Tree Traversals**
   - Inorder, preorder, postorder (recursive)
   - Inorder iterative (stack-based)
   - Level-order (BFS with queue)

2. **Graph Traversal**
   - BFS (adjacency list)
   - DFS (recursive + iterative)

3. **Stack Basics**
   - Valid parentheses
   - Next greater element (monotonic stack)

4. **Tree Essentials**
   - Max depth
   - Validate BST
   - Lowest common ancestor

5. **Quickselect**
   - Kth largest element

---

### Phase 2: Important Additions

6. Longest increasing subsequence (DP)
7. Coin change (DP)
8. Merge K sorted lists (heap)
9. Subsets (backtracking)
10. Number of islands (DFS/BFS)

---

### Phase 3: Round Out Coverage

11. Edit distance (DP)
12. Union-Find basics
13. Dijkstra's shortest path
14. Word search (backtracking)
15. Minimum window substring

---

## 📊 Topic Distribution for FAANG Interviews

**Typical Interview Breakdown:**
- Trees: 25-30%
- Arrays/Strings: 20-25%
- Graphs: 15-20%
- Dynamic Programming: 10-15%
- Linked Lists: 10-15%
- Stacks/Queues: 5-10%
- Heaps: 5-10%
- Others: 5-10%

**Your Current Coverage:**
- ✅ Arrays/Strings: 80%
- ✅ Linked Lists: 90%
- ✅ Sorting/Binary Search: 90%
- ⚠️ Trees: 0%
- ⚠️ Graphs: 20%
- ⚠️ Dynamic Programming: 30%
- ❌ Stacks/Queues: 0%
- ⚠️ Heaps: 40%

---

## 🎓 Study Resources

**Practice Platforms:**
- LeetCode (focus on Easy/Medium for each topic)
- NeetCode 150 (curated list aligned with interviews)
- Blind 75 (essential problems)

**Recommended Order:**
1. Complete all tree basics
2. Add BFS/DFS for graphs
3. Fill stack/queue gaps
4. Expand DP coverage
5. Add backtracking fundamentals

---

## Next Steps

Start with the **Phase 1** list above. Each implementation should include:
- Clear time/space complexity notes
- Test cases
- Edge case handling

Focus on understanding **patterns** rather than memorizing solutions.
