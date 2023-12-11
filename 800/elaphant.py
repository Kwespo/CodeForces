"""
An elephant decided to visit his friend. It turned out that the elephant's house is located
at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step 
the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps 
he need to make in order to get to his friend's house.

Input
The first line of the input contains an integer x (1 ≤ x ≤ 1 000 000) — The coordinate of the friend's house.

Output
Print the minimum number of steps that elephant needs to make to get from point 0 to point x.

Example: 

5 takes 1 move

12 takes 3 moves (5, 4, 3)

"""


fH = int(input()) # Friends house in distance

moves = 0

while fH != 0:
  if fH >= 5:
    fH -= 5
    moves += 1

  elif fH >= 4:
    fH -= 4
    moves += 1

  elif fH >= 3:
    fH -= 3
    moves += 1

  elif fH >= 2:
    fH -= 2
    moves += 1

  elif fH >= 1:
    fH -= 1
    moves += 1

print(moves)