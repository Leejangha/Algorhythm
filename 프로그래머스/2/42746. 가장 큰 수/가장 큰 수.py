def solution(numbers):
    if set(numbers) == {0}:
        return "0"
    # 퀵 정렬 구현
    def Sort(x):
        if len(x) <= 1:
            return x
        
        pivot = x[len(x)//2]
        left, right, equal = [], [], []
        for a in x:
            if a + pivot < pivot + a:
                right.append(a)
            elif a + pivot > pivot + a:
                left.append(a)
            else:
                equal.append(a)
        return Sort(left) + equal + Sort(right)
    
    numbers = list(map(str, numbers))
    return "".join(Sort(numbers))
