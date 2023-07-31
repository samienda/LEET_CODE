class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(names)):
        #     maxi = heights[i]
        #     num = 0
        #     for j in range(i + 1, len(names)):
        #         if maxi < heights[j]:
        #             maxi = heights[j]
        #             num = j
            
        #     if num:
        #         names[i], names[num] = names[num], names[i]
        #         heights[i], heights[num] =heights[num],heights[i]
        
        # return names


        lis = ((names[i],heights[i]) for i in range(len(names)))

        nlis = sorted(lis, key=lambda item:item[1], reverse= True)

        nnlis = [i[0] for i in nlis]

        return nnlis
