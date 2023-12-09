L = int(input())
S = int(input())
R = L
if not (R > S):
    L = R
    R = S
    S = L

while not (S > R):
    R = R - S 

while not (R == 0):
    L = R
    R = S
    S = L
    while not (S > R):
        R = R - S 

print(S)