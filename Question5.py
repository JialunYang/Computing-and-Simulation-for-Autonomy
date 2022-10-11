class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        else:
            dic = {')':'(', ']':'[', '}':'{'}
            temp = []
            for ch in s:
                if ch == '(' or ch == '[' or ch == '{':
                    temp.append(ch)
                elif ch == ')' or ch == ']' or ch == '}':
                    if not temp:
                        return False
                    if dic[ch] == temp[-1]:
                        temp.pop(-1)
                    else:
                        return False
            if not temp:
                return True
            else:
                return False

#T(n)=O(1)