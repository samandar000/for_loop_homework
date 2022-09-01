def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    list2 = []
    k = len(list1)
    for i in range(k):
        list2.append(list1[i].capitalize())
    return list2