1. Aim
Given a frog at the first stair and n stairs, the frog can jump at most k stairs at a time. Find the minimum cost required for the frog to reach the last stair, where the cost of a jump is based on the difference between the heights of the stairs.

2. Software Required
Operating System: Windows 10/11 or Linux
Programming Language: C++, Java, Python
IDE/Editor: VS Code / CodeBlocks / IntelliJ IDEA / PyCharm / Online Compiler

4. Test Cases
Test Case 1:
Input: heights = [10,30,40,50,20], k = 3
Output: 30
Explanation: The frog can jump from stair 1 to stair 2 and then to the last stair. Minimum cost = |30-10| + |20-30| = 20 + 10 = 30.

Test Case 2:
Input: heights = [30,10,60,10,60,50], k = 2
Output: 40
Explanation: The frog chooses jumps in such a way that the total energy difference becomes minimum.

4. Pseudo Code
START
INPUT array heights and integer k
Set n = size of heights
Create dp array of size n and initialize all values with infinity
Set dp[0] = 0
FOR i from 1 to n-1
FOR j from 1 to k
IF i-j is greater than or equal to 0
cost = dp[i-j] + absolute difference between heights[i] and heights[i-j]
dp[i] = minimum of dp[i] and cost
RETURN dp[n-1]
END

8. Learning Outcomes
1. Understand the concept of dynamic programming.
2. Learn how to solve optimization problems using a DP array.
3. Understand how to calculate minimum energy using previous states.
4. Improve logical thinking and problem-solving skills in DSA.
5. Understand implementation in C++, Java, and Python.
