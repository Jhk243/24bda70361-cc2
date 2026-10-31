 1. Aim
Given two strings text1 and text2, return the length of their longest common subsequence (LCS). A
subsequence is a sequence that can be formed by deleting some characters from a string without
changing the order of the remaining characters.

● 2. Software Required
• Operating System: Windows 10/11 or Linux
• Programming Language: C++, Java, Python
• IDE/Editor: VS Code / CodeBlocks / IntelliJ IDEA / PyCharm / Online Compiler

● 3. Test Cases
Test Case 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: the longest common subsequence is "ace", which has length 3.

Test Case 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: both strings are identical, so the whole string "abc" is the common subsequence, giving
length 3.

Test Case 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: the two strings share no characters, so the LCS length is 0.

● 4. Pseudo Code
START
INPUT text1, text2
SET m = LENGTH(text1)
SET n = LENGTH(text2)
CREATE dp[m+1][n+1] FILLED WITH 0
FOR i = 1 TO m
 FOR j = 1 TO n
 IF text1[i-1] == text2[j-1]
 dp[i][j] = dp[i-1][j-1] + 1
 ELSE
 dp[i][j] = MAX(dp[i-1][j], dp[i][j-1])
RETURN dp[m][n]
END

5. Learning Outcomes
1.Understand the dynamic-programming approach to subsequence problems.
2.Learn how to build and fill a 2D DP table from overlapping subproblems.
3.Improve logical thinking and problem-solving skills in DSA.
4.Understand the difference between a subsequence and a substring.
5.Understand implementation in C++, Java, and Python.
