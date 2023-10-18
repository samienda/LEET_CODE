class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for ch in logs:
            if ch == '../':
                if stack:
                    stack.pop()
            else:
                if ch != './':
                    stack.append(ch)
                    

        return len(stack)
                
                    

        