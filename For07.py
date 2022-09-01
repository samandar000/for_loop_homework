def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    answer = 0
    for i in range(N):
        if i%2:
            answer += i
    return answer