class Solution:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        if l1 == l2:
            return True
        else:
            return False

s_ = 'anagram'
list1 = list(s_)
list1.sort()
print(list1)
t_ = 'nagarma'
list2 = list(t_)
list2.sort()
print(list2)

#T(n) = O(nlogn)