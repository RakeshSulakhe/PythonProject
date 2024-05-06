#Add to list

def add_element_to_list(my_list, new_element):
    my_list.append(new_element)
    return my_list


my_list_input = input("Enter the elements of the list separated by spaces: ").split()
my_list = [int(x) for x in my_list_input]

new_element = int(input("Enter the element you want to add: "))
add_element_to_list(my_list, new_element)
print("Updated list:", my_list)

#Remove for list

def remove_element_from_list(my_list, element_to_remove):
    if element_to_remove in my_list:
        my_list.remove(element_to_remove)
    else:
        print("Element not found in the list.")


my_list = input("Enter the elements of the list separated by spaces: ").split()
my_list = [int(x) for x in my_list]

element_to_remove = int(input("Enter the element you want to remove: "))
remove_element_from_list(my_list, element_to_remove)
print("Updated list:", my_list)

# Read the element

def read_list_elements(lst, element):
    if element in lst:
        return element
    else:
        return None

lst_input = input("Enter the elements of the list separated by spaces: ").split()
lst = [int(x) for x in lst_input]
element = int(input("Enter the element you want to search for: "))

result = read_list_elements(lst, element)
if result is not None:
    print("Element is present:", result)
else:
    print("Element is not present in the list.")






