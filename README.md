# Assignment 3: Highest Value Longest Common Sequence (HVLCS)

## Student Information
- Name: Lena Glisic
- UFID: 48575404

---

## Project Description
This project solves the Highest Value Longest Common Sequence (HVLCS) problem using dynamic programming.

Given:
- a set of characters with assigned nonnegative values  
- two input strings A and B  

The program computes:
1. The maximum total value of a common subsequence of A and B  
2. One optimal subsequence that achieves that value  

---

## Repository Structure

ProgrammingAssignment3/
- data/
  - example.in
  - example.out
  - test1.in ... test10.in
- results/
  - runtimes.csv
  - runtime_graph.png
- src/
  - hvlcs.py
  - runtime_test.py
  - plot_runtimes.py
- README.md

---

## Requirements
- Python 3  
- matplotlib (for graph)

Install if needed:
pip3 install matplotlib

---

## How to Run

Run main program:
python3 src/hvlcs.py < data/example.in

Expected output:
9
cb

---

Run runtime tests:
python3 src/runtime_test.py data/test1.in data/test2.in data/test3.in data/test4.in data/test5.in data/test6.in data/test7.in data/test8.in data/test9.in data/test10.in

This generates:
results/runtimes.csv

---

Generate runtime graph:
python3 src/plot_runtimes.py

This generates:
results/runtime_graph.png

---

## Example Input and Output

example.in:
3
a 2
b 4
c 5
aacb
caab

example.out:
9
cb

---

## Assumptions
- All characters in the strings appear in the alphabet list  
- Values are nonnegative integers  
- Any optimal subsequence is acceptable  

---

# Question 1: Empirical Comparison

I created 10 nontrivial input files (test1.in through test10.in), each containing strings of length at least 25.

I measured runtime using runtime_test.py and generated a graph using plot_runtimes.py.

Observation:
All runtimes are very similar because all input sizes are similar. This matches expectations since the algorithm runs in O(n × m) time.

---

# Question 2: Recurrence Equation

Let dp[i][j] be the maximum value of a common subsequence of prefixes.

Base cases:
dp[0][j] = 0  
dp[i][0] = 0  

If characters match:
dp[i][j] = max(
    dp[i-1][j-1] + value(A[i-1]),
    dp[i-1][j],
    dp[i][j-1]
)

If characters do not match:
dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Explanation:
At each step, we either match characters (if equal) or skip one character from one of the strings. This guarantees the optimal solution.

---

# Question 3: Algorithm and Big-Oh

Pseudocode:
for i from 1 to n:
    for j from 1 to m:
        if A[i-1] == B[j-1]:
            dp[i][j] = max(
                dp[i-1][j-1] + value,
                dp[i-1][j],
                dp[i][j-1]
            )
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Then reconstruct subsequence by backtracking.

Time Complexity:
O(n * m)

Space Complexity:
O(n * m)

