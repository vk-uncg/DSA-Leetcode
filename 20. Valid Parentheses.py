class Solution:
    def isValid(self, s: str) -> bool:
        opening = set('([{')
        matches = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []

        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False
                last_opened = stack.pop()
                if (last_opened, paren) not in matches:
                    return False
        
        return len(stack) == 0