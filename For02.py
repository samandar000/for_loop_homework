def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    list1 = ''
    list = [] 
    m = ','
    for i in range(n):
        list.append(str(i))
        str(list)
        k = m.join(list)
    return k

