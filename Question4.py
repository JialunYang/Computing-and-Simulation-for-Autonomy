class Solution:
    def __init__(self, s):
        self.s = s

    def check(self, s):
        letter = []
        for i in s:
            if i in letter:
                return False
            else:
                letter.append(i)
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length

        maxLen = 1
        for i in range(length):
            for j in range(i + 1, length):
                temp = s[i:j + 1]
                if self.check(temp) == True:
                    maxLen = max(len(temp), maxLen)
        return maxLen


list1 = ['abcabcbb']
Solution(list1)