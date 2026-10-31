1. Aim
Given an m x n 2D binary grid where '1' represents land and '0' represents water, return the number of islands. An island is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

2. Software Required
Operating System: Windows 10/11 or Linux
Programming Language: C++, Java, Python
IDE/Editor: VS Code / CodeBlocks / IntelliJ IDEA / PyCharm / Online Compiler

3. Test Cases
Test Case 1:
Input: grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
Output: 1
Explanation: All connected land cells form one single island.

Test Case 2:
Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
Output: 3
Explanation: There are three separate groups of connected land cells, so the answer is 3.

4. Pseudo Code
START
INPUT 2D grid
IF grid is empty
RETURN 0
Set count = 0
Set rows = number of rows in grid
Set cols = number of columns in grid
FOR each cell in the grid
IF current cell is land, that is "1"
Increase count by 1
Call DFS on current cell to mark the complete island as visited
DFS(row, col)
IF row or col is outside grid boundary OR current cell is water, that is "0"
RETURN
Mark current cell as visited by changing "1" to "0"
Call DFS for up direction
Call DFS for down direction
Call DFS for left direction
Call DFS for right direction
RETURN count
END

8. Learning Outcomes
1. Understand the concept of grids and 2D matrix traversal.
2. Learn how to use Depth First Search to explore connected components.
3. Understand how islands are counted by marking visited land cells.
4. Improve problem-solving skills in graph and matrix-based DSA problems.
5. Understand implementation in C++, Java, and Python.
