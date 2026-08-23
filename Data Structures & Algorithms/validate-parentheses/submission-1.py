class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        opens = {'(', '{', '['}
        for ch in s:
            if ch in opens:
                parentheses.append(ch)
            else:
                if len(parentheses) == 0:
                    return False
                elif ch == ')' and parentheses[-1] == '(':
                    parentheses.pop()
                elif ch == '}' and parentheses[-1] == '{':
                    parentheses.pop()
                elif ch == ']' and parentheses[-1] == '[':
                    parentheses.pop()
                else:
                    return False
        return len(parentheses) == 0