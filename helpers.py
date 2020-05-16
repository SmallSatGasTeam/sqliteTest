def twoDize(array, width):
    """
    Takes a one dimensional array and converts it into a non-ragged array of a specified width.
    """
    count = 0
    output = []
    temp = []
    while len(array) > 0:
        temp.append(array.pop())
        if len(temp) == width:
            output.append(temp)
            temp = []
    return output


def printArray(arr):
    """
    Prints a two dimensional list with a new line between each entry.
    """
    for entry in arr:
        print(entry)
