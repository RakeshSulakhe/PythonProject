#Add to list

def add_to_list(lst,element):
    lst.append(element)
    return lst

result = add_to_list([10,20,30,40],50)
print("Updated list after adding element:", result)

#Remove for list

def remove_for_list(lst,element):
    lst.remove(element)
    return lst

res =  remove_for_list([10,20,30,40,50],40)
print("Updated list after removing element:", res)

# Read the element

def read_list_elements(lst,element):
    while element in lst:
        return element

rest = read_list_elements([10,20,30,40,50],40)
print("Element is present",rest)