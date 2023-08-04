def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    return  data.index(min(data))
data=[7,6,5,1,3,9]
print(find_min_index(data))



