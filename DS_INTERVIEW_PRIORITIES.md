# Data Science Interview Algorithm Priorities

## Current Coverage: **85-90% Complete** for DS Roles

---

## 🎯 What Data Science Interviews Test

**Key Difference from SWE:**
- **Less emphasis** on complex data structures (trees, graphs, stacks)
- **More emphasis** on problem-solving, optimization, and data manipulation
- **Focus areas**: Arrays, optimization, statistics, basic algorithms

**Typical DS Coding Interview (60-90 min):**
- 1-2 medium problems (array/string manipulation, optimization)
- Focus on clean code, edge cases, and complexity analysis
- May include system design or ML system design instead of hard coding

---

## ✅ Your Strong Areas (Already Covered)

### **Arrays & Data Manipulation** (Critical for DS - 95% coverage)
- ✓ Kadane's algorithm (max/min subarray)
- ✓ Sliding window (fixed and variable size)
- ✓ Two pointers (palindrome, duplicates, sorted arrays)
- ✓ Prefix sums (1D and 2D)
- ✓ Binary search (standard + rotated variants)

**Why it matters:** Data cleaning, feature engineering, time series analysis

---

### **Hash Maps/Dictionaries** (Critical for DS - 100% coverage)
- ✓ Two sum, frequency counting
- ✓ Group anagrams
- ✓ Max frequency operations

**Why it matters:** Data aggregation, categorical encoding, duplicate detection

---

### **Sorting & Searching** (Important - 90% coverage)
- ✓ Quick sort, merge sort, heap sort
- ✓ Binary search variants

**Why it matters:** Data preprocessing, efficient lookups

---

### **Optimization Algorithms** (Important - 85% coverage)
- ✓ Greedy: Activity selection, fractional knapsack
- ✓ Stock profit problems (multiple variants)
- ✓ Dynamic programming: 0/1 Knapsack

**Why it matters:** Resource allocation, budget optimization, scheduling

---

### **Statistical & ML Algorithms** (DS-specific - Good coverage)
- ✓ Simple moving average (SMA)
- ✓ Forecasting algorithms
- ✓ Mean squared error (loss functions)

**Why it matters:** Core DS skills, model evaluation

---

### **Linked Lists** (Less critical for DS - 90% coverage)
- ✓ Reverse, cycle detection
- ✓ Merge sorted lists
- ✓ Find middle, remove nth node

**Why it matters:** Occasionally tested, good problem-solving practice

---

### **Recursion** (Important - 100% coverage)
- ✓ Fibonacci, factorial, GCD
- ✓ Permutations, power, Tower of Hanoi

**Why it matters:** Shows algorithmic thinking, problem decomposition

---

## ⚠️ Gaps to Address (Prioritized for DS Roles)

### **Priority 1: HIGH (Add These Next)**

#### 1. **Top-K Problems** (Very Common in DS)
**Missing:**
- Kth largest element (quickselect algorithm)
- Kth smallest element
- Top K frequent elements

**Why critical:** 
- Percentile calculations
- Outlier detection
- Feature selection
- Ranking systems

**Implementation:** Use quickselect (O(n) average) or heap (O(n log k))

---

#### 2. **Heap Operations** (Common in DS)
**Have:** Heap sort, K closest points
**Missing:**
- Merge K sorted lists (distributed data)
- Find median from data stream
- Task scheduler

**Why critical:**
- Merging distributed data
- Running statistics
- Priority queues for simulations

---

#### 3. **More Dynamic Programming** (Optimization Problems)
**Have:** 0/1 Knapsack
**Missing:**
- Longest increasing subsequence (LIS)
- Coin change
- House robber
- Climbing stairs (DP version)

**Why critical:**
- Shows optimization thinking
- Resource allocation problems
- Common in Applied Scientist roles

---

### **Priority 2: MEDIUM (Nice to Have)**

#### 4. **Basic Graph Algorithms** (Network Analysis)
**Have:** Topological sort
**Missing:**
- BFS traversal (breadth-first search)
- DFS traversal (depth-first search)
- Number of islands
- Connected components

**Why useful:**
- Social network analysis
- Recommendation systems
- Feature graph traversal
- Customer journey mapping

---

#### 5. **String Algorithms** (If NLP-focused)
**Have:** Palindrome, anagrams
**Missing:**
- Longest common subsequence (LCS)
- Edit distance (Levenshtein)
- Minimum window substring

**Why useful:**
- Text similarity
- Autocorrect/autocomplete
- String matching in logs

---

#### 6. **Basic Tree Algorithms** (Less critical than SWE)
**Missing:**
- Binary tree traversals (inorder, preorder, postorder)
- Level-order traversal (BFS)
- Max depth / height
- Validate BST

**Why useful:**
- Decision tree understanding
- Hierarchical data structures
- Occasionally tested in interviews

---

### **Priority 3: LOW (Can Skip for Most DS Roles)**

#### 7. **Stacks & Queues**
- Valid parentheses
- Monotonic stack problems

**When needed:** Data pipeline engineering, parser building (rare)

---

#### 8. **Backtracking**
- Subsets, combinations
- N-Queens, word search

**When needed:** Almost never in pure DS roles; more common in research/algorithm-heavy roles

---

#### 9. **Bit Manipulation**
- XOR tricks, bit counting

**When needed:** Very rare in DS interviews

---

#### 10. **Advanced Tree/Graph**
- Dijkstra's shortest path
- Union-Find / Disjoint Set

**When needed:** Applied Scientist roles at FAANG focusing on algorithms

---

## 📋 Recommended Study Plan for DS Interviews

### **Week 1-2: Fill Critical Gaps**
1. Implement quickselect (Kth largest element)
2. Solve "Top K Frequent Elements" (heap-based)
3. Add 2-3 more DP problems (LIS, coin change)
4. Implement "Merge K Sorted Lists" (heap)

### **Week 3-4: Round Out Coverage**
5. Basic BFS/DFS for graphs
6. Binary tree traversals (recursive versions)
7. String algorithms if NLP-focused (edit distance, LCS)

### **Week 5+: Practice & Review**
8. LeetCode Easy/Medium in your gap areas
9. Review all existing implementations
10. Practice explaining time/space complexity

---

## 🎓 Interview Breakdown by Company Type

### **FAANG Applied Scientist (Amazon, Meta, Google)**
- **Coding:** 40-50% of interview loop
- **Focus:** Medium problems, optimization, some DP
- **Your readiness:** 85% → Add Priority 1 + 2
- **Tree questions:** 10-15% (basic traversals sufficient)

### **Mid-Tier Tech DS (Spotify, Airbnb, Uber)**
- **Coding:** 30-40% of interview loop
- **Focus:** Array manipulation, SQL, statistics
- **Your readiness:** 90% → Add Priority 1 only
- **Tree questions:** Rare (5-10%)

### **Analytics-Heavy DS (Finance, Consulting)**
- **Coding:** 20-30% of interview loop
- **Focus:** SQL, Python pandas, basic algorithms
- **Your readiness:** 95%+ → Current coverage sufficient
- **Tree questions:** Almost never

---

## 💡 Key Differences: DS vs SWE Interviews

| Topic | SWE Importance | DS Importance | Your Coverage |
|-------|---------------|---------------|---------------|
| Arrays/Strings | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 95% ✅ |
| Hash Maps | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 100% ✅ |
| Trees | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 0% ⚠️ |
| Graphs | ⭐⭐⭐⭐ | ⭐⭐⭐ | 20% ⚠️ |
| Dynamic Programming | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 30% ⚠️ |
| Heaps | ⭐⭐⭐ | ⭐⭐⭐⭐ | 40% ⚠️ |
| Linked Lists | ⭐⭐⭐⭐ | ⭐⭐ | 90% ✅ |
| Stacks/Queues | ⭐⭐⭐⭐ | ⭐ | 0% |
| Backtracking | ⭐⭐⭐ | ⭐ | 0% |
| Optimization | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 85% ✅ |

---

## 🔥 Top 10 Must-Add Algorithms (DS-focused)

Prioritized list to go from 85% → 98%:

1. **Kth Largest Element** (quickselect) - Percentiles, ranking
2. **Top K Frequent Elements** (heap) - Frequency analysis
3. **Merge K Sorted Lists** (heap) - Distributed data merging
4. **Longest Increasing Subsequence** (DP) - Trend analysis
5. **Coin Change** (DP) - Optimization classic
6. **BFS Graph Traversal** (adjacency list) - Network analysis
7. **DFS Graph Traversal** (recursive) - Network analysis
8. **Binary Tree Inorder Traversal** (recursive) - Basic trees
9. **Edit Distance** (DP) - String similarity (if NLP)
10. **Find Median from Data Stream** (two heaps) - Running statistics

---

## 📚 Practice Resources (DS-specific)

### **LeetCode Lists:**
- **NeetCode 150**: Skip hard tree/graph problems
- **Blind 75**: Focus on arrays, DP, heaps
- **Top Interview Questions**: Filter by Easy/Medium

### **Focus Topics:**
- Arrays: 50 problems
- Dynamic Programming: 20-30 problems
- Heaps: 10-15 problems
- Graphs: 10-15 problems (BFS/DFS basics)
- Trees: 10 problems (basic traversals only)

### **Time Allocation:**
- 60% Arrays, strings, hash maps (your strength)
- 25% DP and heaps (fill gaps)
- 15% Graphs and trees (basics only)

---

## ✅ Summary: Your Next Steps

**You're in great shape!** To reach 98% readiness:

1. ✅ **This weekend:** Implement quickselect and Top K Frequent
2. ✅ **Next week:** Add 2-3 DP problems (LIS, coin change)
3. ✅ **Week after:** Merge K sorted lists, basic BFS/DFS
4. ✅ **Optional:** Basic tree traversals if time permits

**Bottom line:** You already have the foundation. Adding 5-10 more implementations will make you very competitive for any DS role.
