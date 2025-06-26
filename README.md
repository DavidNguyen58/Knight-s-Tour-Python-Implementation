# Knight-Tour-Python-Implementation

## Introduction
The knight's tour is one of popular problems in Computer Science where the problem seeks to find if there is a tour of a knight which visits all the squares on the board of size n*n, and every square can not be re-visited.

## Approach
The problem could be solved via backtracking where we try to consider all the possible moves at the current position of the knight the knight could take and extend the search. If the knight hits a dead end, where no further search is possible, then we backtrack to the previous position and search other moves. If there is no solution after all the possible searches, then we return False. Otherwise, we will return True and print out the tour of the Knight. The time complexity if this brute-force algorithm would be $O(8^n)$ where 8 is the number of possible moves at every position and n is the number of squares on the board.

However, we could be a little more clever here by including a heuristic in our search. One of the popular heuristics for this problem is Warnsdorf Heuristic. During the exploration state, the heuristic will move the Knight to a position with the least number of possible moves, helping to increase the speed of finding the solution if it exits. Additionally, the heuristic also allows to generate a possible solution for a large state of n greater than 20.






