
import numpy as np
print("Enter the tiles 0 to 8")
l = []

i = 0
for i in range(3):
    row = []
    for j in range(3):
        v = int(input())
        row.append(v)
    l.append(row)
    
goal_state = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

n = 0 
for i in range(3):
    for j in range(3):
        if l[i][j] != goal_state[i][j]:
            n +=1
print("This is the state you entered :")
for row in l:
    print(row)

print("Misplaced tiles :")
print(n)
