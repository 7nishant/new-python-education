#What is difference between push and append in list?
# Append method adds an element at the end of an existing list. Common error: does not return the new list, just
# modifies the original.
#push method inserts the element at the given index, shifting elements to the right.

def my_list():
    list_one = [1, 2, 3]
    list_one.append(4)
    return list_one

print(my_list())

def my_list():
    list_one = [1, 2, 3]
    list_one.insert(1, 4)
    return list_one

print(my_list())


