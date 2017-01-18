"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = []
    # Move tiles to the left
    for num in line:
        if num != 0:
            new_line.append(num)
    # Fill the rest with zeros
    while len(new_line) < len(line):
        new_line.append(0)

    for dummy_num in range(len(line) - 1):
        if new_line[dummy_num] == new_line[dummy_num + 1]:
            new_line[dummy_num] *= 2
            new_line.pop(dummy_num + 1)
            new_line.append(0)

    return new_line

list1 = [4, 2, 2, 4]
list2 = [2, 0, 2, 4]
list3 = [2, 2, 4, 4]
list4 = [2, 2, 2, 2, 2]
#merge(list1)
print(merge(list1))
print(merge(list2))
print(merge(list3))
print(merge(list4))
