def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    data.sort()
    for i in range(len(data)):
        if data[len(data)-i-1]%2==1:
            return data[len(data)-i-1]
   
    
data=[1,2,3,4,5,6,17,18,4]
print(find_max_odd(data))
