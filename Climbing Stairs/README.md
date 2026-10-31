1. Problem Statement
You are climbing a staircase. It takes n steps to reach the top. Each time you may climb either 1 or 2
steps. In how many distinct ways can you climb to the top?
• Each move climbs exactly 1 step or 2 steps.
• Count the distinct ordered sequences of moves whose step sizes add up to n.

Input Format
• n: an integer giving the total number of steps to climb (1 <= n <= 45).
• There is no other input; the answer depends only on n.

Output Format
• Return the number of distinct ways to reach the top.
Constraints
• 1 <= n <= 45
• The result fits in a 32-bit signed integer for every valid n.
• Only step sizes of 1 and 2 are allowed; no larger jumps.

Note: Order matters: climbing 1 then 2 is counted separately from 2 then 1. This is exactly why
the number of ways grows like the Fibonacci sequence.

2. Examples / Test Cases
The table below summarises the key test cases:
n Output Example Ways Why
n = 1 1 1 Only one way to climb: a single 1-step.
n = 2 2 1+1 | 2 Two single steps (1+1) or one double step (2).
n = 3 3 1+1+1 | 1+2 | 2+1 Three distinct orderings: 1+1+1, 1+2, 2+1.
n = 4 5 1+1+1+1 | 1+1+2 | 1+2+1
| 2+1+1 | 2+2
ways(4) = ways(3) + ways(2) = 3 + 2 = 5.
n = 5 8 8 sequences (Fibonacci) ways(5) = ways(4) + ways(3) = 5 + 3 = 8, a
Fibonacci value.

3. Edge Cases
Boundary Inputs to Consider
• n = 1: There is exactly one way (a single 1-step), so the answer is 1.
• n = 2: The first case with two options (1+1 or 2), giving an answer of 2.
• Base cases: Handle n = 1 and n = 2 directly before the loop begins.
• Order matters: 1+2 and 2+1 are different sequences and counted separately.
• Large n (up to 45): The count grows quickly, but still fits in a 32-bit int.
• Loop bounds: The recurrence runs from i = 3 to n once the base cases are set.

Memory: A rolling two-variable solution avoids storing the entire DP array.
• Allowed moves: Only 1-step and 2-step moves are permitted; nothing larger.

4. Brute Force Approach
Core Idea
Solve straight from the definition with recursion: to reach step n you arrive either from step n-1 (a 1-
step) or step n-2 (a 2-step), so ways(n) = ways(n-1) + ways(n-2), with base cases ways(1) = 1 and
ways(2) = 2. A naive recursion recomputes the same subproblems again and again.
Pseudocode
def climb(n):
 if n <= 2:
 return n
 return climb(n - 1) + climb(n - 2)
print(climb(5)) # 8
Complexity
Approach Time Complexity Space Complexity
Brute Force O(2^n) O(n)
Why it fails: Plain recursion branches into two calls at every level and recomputes identical
subproblems. For n = 45 this performs billions of repeated calls and is exponentially slow.
