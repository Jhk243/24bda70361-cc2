1. Aim
Given an integer n, determine the number of distinct ways to climb to the top of a staircase
with n steps. At each step, you can climb either 1 step or 2 steps at a time.

● 2. Software Required
• Operating System: Windows 10/11 or Linux
• Programming Language: C++, Java, Python
• IDE/Editor: VS Code / CodeBlocks / IntelliJ IDEA / PyCharm / Online Compiler

● 3. Test Cases
Test Case 1:
Input: n = 2
Output: 2
Explanation: there are two ways - (1 step + 1 step) or (2 steps).

Test Case 2:
Input: n = 3
Output: 3
Explanation: the three ways are 1+1+1, 1+2, and 2+1.

Test Case 3:
Input: n = 5
Output: 8
Explanation: each count is the sum of the previous two, giving the Fibonacci-like value 8.

4. Pseudo Code
START
INPUT n
IF n <= 2
 RETURN n
SET prev1 = 1
SET prev2 = 2
FOR i = 3 TO n
 SET current = prev1 + prev2
 prev1 = prev2
 prev2 = current
RETURN prev2
END

 5. Learning Outcomes
1.Understand the dynamic-programming approach to counting problems.
2.Learn how the problem reduces to the Fibonacci recurrence.
3.Improve logical thinking and problem-solving skills in DSA.
4.Understand how to optimise space from O(n) to O(1) using two rolling variables.
5.Understand implementation in C++, Java, and Python.
