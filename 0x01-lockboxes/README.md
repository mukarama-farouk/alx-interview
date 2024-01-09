<h1>0x01. Lockboxes</h1>

<h3>This implementation uses a depth-first search (DFS) approach to explore the boxes and keeps track of the keys using a set. The function returns True if all boxes can be opened and False otherwise. The provided example usage assumes that each box contains a list of keys to other boxes, and an empty list represents a box with no keys.</h3>
--------------------------------------------------------------------------------------------------------------------------------------------
Requirements
General
1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. The first line of all your files should be exactly #!/usr/bin/python3
5. A README.md file, at the root of the folder of the project, is mandatory
6. Your code should be documented
7. Your code should use the PEP 8 style (version 1.7.x)
8. All your files must be executable

-------------------------------------------------------------------------------------------------------------------------------------------
Tasks
0. Lockboxes
mandatory
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
