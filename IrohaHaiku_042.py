"""
Time limit : 2sec / Memory limit : 256MB

Score : 100 points

Problem Statement
Iroha loves Haiku. Haiku is a short form of Japanese poetry.
A Haiku consists of three phrases with 5, 7 and 5 syllables, in this order.

To create a Haiku, Iroha has come up with three different phrases.
These phrases have A, B and C syllables, respectively.
Determine whether she can construct a Haiku by using each of the phrases once, in some order.

Constraints
1≦A,B,C≦10

"""

# print("input the number of syllables: ")
A, B, C  = map(int, input().split())
if A and B and C >= 1:
        if A and B and C <= 10:
             if A == 5 and B == 5 and C == 7: print('YES')
             elif A == 5 and B == 7 and C == 5: print('YES')
             elif A == 7 and B == 5 and C == 5: print('YES')
             else:
                 print('NO')


n = list(map(int, input().split()))
if n.count(5) == 2 and n.count(7) == 1:
    print('YES')
else:
    print('NO')


