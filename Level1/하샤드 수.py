def solution(x):
    return x % sum(list(map(int, list(str(x))))) == 0

'''
def solution(x):
    if x % sum(list(map(int, list(str(x))))) == 0:
        return True
    return False
'''
