1. Aim
Given an integer array coins representing different coin denominations and an integer amount, return the fewest number of coins required to make up that amount. You may use each coin denomination an unlimited number of times. If the amount cannot be made up, return -1.

2. Software Required
Operating System: Windows 10/11 or Linux
Programming Language: C++, Java, Python
IDE/Editor: VS Code / CodeBlocks / IntelliJ IDEA / PyCharm / Online Compiler

4. Test Cases
Test Case 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: The minimum number of coins required is 3 because 11 = 5 + 5 + 1.

Test Case 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: It is not possible to make amount 3 using only coin 2.

4. Pseudo Code
START
INPUT coins array and amount
Create dp array of size amount + 1
Fill dp array with amount + 1
Set dp[0] = 0
FOR i = 1 to amount
FOR each coin in coins
IF i - coin is greater than or equal to 0
dp[i] = minimum of dp[i] and dp[i - coin] + 1
IF dp[amount] is greater than amount
RETURN -1
ELSE
RETURN dp[amount]

END
