"""
Student code for Word Wrangler game
"""

import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    list_copy = list(list1)
    to_remove = []
    if len(list1) > 1:
        for idx in range(0, len(list1) - 1):
            if list_copy[idx] == list_copy[idx + 1]:
                to_remove.append(list_copy[idx])
    for item in to_remove:
        list_copy.remove(item)

    return list_copy


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    intersection = []
    list1_copy = list(list1)
    list2_copy = list(list2)
    while list1_copy and list2_copy:
        if list1_copy[0] < list2_copy[0]:
            list1_copy.pop(0)
        elif list1_copy[0] > list2_copy[0]:
            list2_copy.pop(0)
        else:
            intersection.append(list1_copy[0])
            list2_copy.pop(0)
            list1_copy.pop(0)
    return intersection


# Functions to perform merge sort
def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    result = []
    list1_copy = list(list1)
    list2_copy = list(list2)
    while list1_copy and list2_copy:
        if list1_copy[0] < list2_copy[0]:
            result.append(list1_copy[0])
            list1_copy.pop(0)
        elif list1_copy[0] > list2_copy[0]:
            result.append(list2_copy[0])
            list2_copy.pop(0)
        else:
            result.append(list1_copy[0])
            result.append(list2_copy[0])
            list2_copy.pop(0)
            list1_copy.pop(0)
    if list1_copy:
        for item in list1_copy:
            result.append(item)
    elif list2_copy:
        for item in list2_copy:
            result.append(item)
    return result


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) == 1 or len(list1) == 0:
        return list1
    else:
        part1 = merge_sort(list1[:len(list1) // 2])
        part2 = merge_sort(list1[len(list1) // 2:])
        return merge(part1, part2)


def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    all_strings = []
    if len(word) == 0:
        all_strings.append("")
    else:
        current_letter = word[0]
        rest_strings = gen_all_strings(word[1:])
        for item in rest_strings:
            all_strings.append(item)
            for idx in range(len(item) + 1):
                all_strings.append(item[:idx] + current_letter + item[idx:])

    return all_strings


def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    file = open(filename, "r")
    data = file.read()

    return data


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

if __name__ == "__main__":
    run()
