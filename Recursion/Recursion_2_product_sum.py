# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

# O(n) Time | O(d) Space

def productSum(array, multiplier=1):

    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier
