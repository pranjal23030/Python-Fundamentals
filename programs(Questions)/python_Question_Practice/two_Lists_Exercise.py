a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6, 9, 2, 1, 3, 5]


def find_common_elements(list1, list2):
    common_elements = []
    for item1 in list1:
        if item1 in list2 and item1 not in common_elements:
            common_elements.append(item1)
    return common_elements


result = find_common_elements(a, b)
print("Common elements within the lists are: ", result)
