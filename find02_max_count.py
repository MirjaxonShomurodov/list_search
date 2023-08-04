def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    return data.count(max(data))
data=[2,4,7,7,6,7,3,7]

print(find_max_count(data))