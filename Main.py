import list_functions

def main():
    my_list_input = input("Enter the elements of the list separated by spaces: ").split()
    my_list = [int(x) for x in my_list_input]

    new_element = int(input("Enter the element you want to add: "))
    add_element_to_list(my_list, new_element)
    print("Updated list:", my_list)

if __name__ == "__main__":
    main()

# Remove_Element

def main():
    my_list_input = input("Enter the elements of the list separated by spaces: ").split()
    my_list = [int(x) for x in my_list_input]

    element_to_remove = int(input("Enter the element you want to remove: "))
    remove_element_from_list(my_list, element_to_remove)
    print("Updated list:", my_list)

if __name__ == "__main__":
    main()


# Read_list

def main():
    lst_input = input("Enter the elements of the list separated by spaces: ").split()
    lst = [int(x) for x in lst_input]

    element = int(input("Enter the element you want to search for: "))

    result = read_list_elements(lst, element)
    if result is not None:
        print("Element is present:", result)
    else:
        print("Element is not present in the list.")

if __name__ == "__main__":
    main()


