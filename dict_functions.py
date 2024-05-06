# Add to dictionary
def add_element_to_dict():
    my_dict = {"1":"A","2":"B"}
    print("Enter key-value pairs to add to the dictionary (press Enter for key to stop):")
    while True:
        key = input("Enter key: ")
        if key == "":
            break
        value = input("Enter value: ")
        my_dict[key] = value

    return my_dict

user_dict = add_element_to_dict()
print("Dictionary after adding elements:",user_dict)

# # Remove a element from dictionary
#
# def remove_element_from_dictionary(my_dict):
#     print("Current dictionary:")
#     print(my_dict)
#
#     key_to_remove = input("Enter the key to remove: ")
#
#     if key_to_remove in my_dict:
#         del my_dict[key_to_remove]
#         print("Element with key '{}' removed successfully.".format(key_to_remove))
#     else:
#         print("Key '{}' not found in the dictionary.".format(key_to_remove))
#
#     return my_dict
#
# my_dictionary = {'a': 1, 'b': 2, 'c': 3}
# my_dictionary = remove_element_from_dictionary(my_dictionary)
# print("Updated dictionary:",my_dictionary)
#
#
# # Read element from dictionary
#
# def read_dictionary_elements(my_dict,element):
#     for key, value in my_dict.items():
#         print("Key:", key, "| Value:", value)
#
# read_dictionary_elements({"1":"A","2":"B","3":"C"},{"1":"A"})