class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = []
        rad = []

        n = len(senate)

        for i in range(n): # O(n)
            if senate[i] == 'R':
                rad.append(i)
            else:
                dire.append(i)

        while dire and rad: #O(n/2)
            r, d = rad.pop(0), dire.pop(0)
            if r < d :
                rad.append(r + n)
            else:
                dire.append(d + n)


        return "Radiant" if rad else "Dire"

        # 




        