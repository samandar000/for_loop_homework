def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    i=0
    answer=0
    list1 = range(A,B)
    list1 = list(list1)
    while i < len(list1):
        answer = answer + list1[i]
        i+=1
    
    return answer
