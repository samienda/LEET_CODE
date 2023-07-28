class Solution:
    import sys
    # sys.setrecursionlimit(100000000)
    def isPalindrome(self, s: str) -> bool:
        def checker(word):
            # if not word:
            #     return True
            # if word[0] != word[len(word) - 1]:
            #     return False

            # return checker(word[1:len(word) - 1])


            # SINCE RECURSION TAKES A LOT OF MEMORY LET'S FIND ANOTHER WAY 
            
            flag = True
            front = 0
            end = len(word) - 1
            while word and flag and end > front:
                if word and  word[front] != word[end]: 
                    flag = False 
                front += 1
                end -= 1


            return flag 


        import re
        # THESE ARE REGULAR EXPRESSIONS YOU CAN MODIFY YOUR STRING USING RE MODULE IT HAVE METHODS LIKE SUB, FINDALL, MATCH, SPLIT, SEARCH .....
        # THE FORMAT FOR SUB IS RE.SUB(THE CHARACTER TO REPLACE USE ^ FOR NEGATION ,TO REPLACE WITH, AND THE LETTER TO MODIFY)

        # word = re.sub(r'[^a-zA-z0-9]','', s)
        



        # THERE IS EVEN A BETTER WAY [^\W] THIS MEANS ANY THING THAT IS A LETTER OR  DIGIT AND UNDERSCORES
        word = re.sub(r'[^\w]', '', s)
        word = re.sub(r'_', '', word)

        return checker(word.lower())