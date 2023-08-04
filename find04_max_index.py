def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    return data.index(max(data))
data=[7,6,5,1,3,9]
print(find_max_index(data))
