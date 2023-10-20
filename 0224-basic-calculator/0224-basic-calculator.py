class Solution:
    def calculate(self, s: str) -> int:
        output = 0
        curr = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char) # converting the str to int
                # curr = int(char)          
            elif char  in "+-":
                output += (curr * sign)
                curr = 0
                if char == "+":
                    sign = 1
                else:
                    sign = -1
            elif char == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif char == ")":
                output += (curr * sign)
                output *= stack.pop()
                output += stack.pop()
                curr = 0


        return output + (curr * sign)

        # if digit:update the curr
        # if + or -:
        #     - calculate the output
        #     - reset the curr to 0
        #     - change the sign based on the operator
        # if (:
        #     - append the output to the stack
        #     - append the sign to the stack
        #     - reset the output, assign sign to 1
        # if ):
        #     - update the output
        #     - reset the curr


