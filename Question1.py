def solution(list, num): 
    '''type in your solution, find a and b in array that a+b=num'''
    for a in list:
        a = int(a)
        for b in list:
            b = int(b)
            if a != b and a+b == num:
                return a,b

numbers = [0, 21, 78, 19, 90, 13]
print(solution(numbers, 21))
print(solution(numbers, 25))

#T(n)=O(n^2)