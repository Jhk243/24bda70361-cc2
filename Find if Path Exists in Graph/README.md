 1. Aim
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges
are given as a 2D array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between
vertex ui and vertex vi. Given edges and the integers n, source and destination, determine whether a
valid path exists from source to destination, returning true if such a path exists and false otherwise.

● 2. Software Required
• Operating System: Windows 10/11 or Linux
• Programming Language: C++, Java, Python
• IDE/Editor: VS Code / CodeBlocks / IntelliJ IDEA / PyCharm / Online Compiler

● 3. Test Cases
Test Case 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: there are two paths from vertex 0 to vertex 2, namely 0 -> 1 -> 2 and the direct edge 0 -

Test Case 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: vertices 0, 1 and 2 form one component while vertices 3, 4 and 5 form another, so
vertex 5 cannot be reached from vertex 0.

Test Case 3:
Input: n = 1, edges = [], source = 0, destination = 0
Output: true
Explanation: the source and the destination are the same vertex, so the path is the vertex itself and
no edge is needed.

● 4. Pseudo Code
START
INPUT n, edges, source, destination
CREATE adj[0..n-1] AS EMPTY LISTS
FOR EACH (u, v) IN edges
 adj[u].ADD(v)
 adj[v].ADD(u)
CREATE visited[0..n-1] FILLED WITH FALSE
CREATE EMPTY QUEUE q
q.PUSH(source)
visited[source] = TRUE
WHILE q IS NOT EMPTY
 node = q.POP_FRONT()
 IF node == destination
 RETURN TRUE
 FOR EACH nbr IN adj[node]
 IF visited[nbr] == FALSE
 visited[nbr] = TRUE
 q.PUSH(nbr)
RETURN FALSE
END

5. Learning Outcomes
1.Understand how an undirected graph is stored as an adjacency list.
2.Learn breadth-first search and how marking vertices as visited prevents infinite loops.
3.Understand connected components and what graph connectivity means.
4.Compare the BFS, DFS and Disjoint Set Union approaches to the same problem.
