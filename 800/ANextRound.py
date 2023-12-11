"""
"Contestant who earns a score equal to or greater than the k-th place 
finisher's score will advance to the next round, 
as long as the contestant earns a positive score..." — an excerpt 
from contest rules.

A total of n participants took part in the contest (n ≥ k), and you 
already know their scores. Calculate how 
many participants will advance to the next round.

Input
The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50)
separated by a single space.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100),
here ai is the score earned
by the participant who got the i-th place. The given sequence is non-increasing
(that is, for all i from 1
to n - 1 the following condition is fulfilled: ai ≥ ai + 1).

Output
Output the number of participants who advance to the next round.


Note
In the first example the participant on the 5th place earned 7 points. As the participant on the 6th place also earned 7 points, 
there are 6 advancers.

In the second example nobody got a positive score.

"""
passing = 0 # How many people are passing

nAndk = input().split() # Gets the amount of people (n), and the position in the list they need to be larger, or equal to (k) and splits into a list

score = input().split() # Gets all the scores and split them into a list

for i in range(int(nAndk[0])): # Loops for the amount of people (n)
  if int(score[i]) >= int(score[int(nAndk[1]) - 1]) and int(score[i]) > 0: # If the score is larger then the k position in the list, and more then 0
    # It is int(score[int(nAndk[1]) - 1]) because lists start at 0 so position 5 (for example) would be 4 but without minusing 1 it gives position 6
    passing =+ passing + 1 # Pass

print(passing)