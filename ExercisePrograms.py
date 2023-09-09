# WAPP to print unique elements in a list and order of insertion must be preserved

def unique_elements(li):
    unique_li = []

    for el in li:
        if el not in unique_li:
            unique_li.append(el)

    print(unique_li)


sample_input = [10, 30, 20, 20, 10, 30, 60, 23, 34, 23]
unique_elements(sample_input)


# WAPP to reverse li
def rev_list(li):
    li.sort(reverse=True)
    print(li)


sample_input = [10, 20, 30, 40, 50]
rev_list(sample_input)


# WAPP to convert Tuple to List
def tuple_to_list(tup):
    li = list(tup)
    print(li)


sample_input = (10, 20, 30, 20, 40, 50)
tuple_to_list(sample_input)


# WAPP to find intersection of 2 lists
def list_intersection(li1, li2):
    li_intersection = list(set(li1).intersection(li2))
    print(li_intersection)


li1 = [1, 3, 2, 4, 5]
li2 = [3, 2, 5, 6, 7, 8]
list_intersection(li1, li2)
