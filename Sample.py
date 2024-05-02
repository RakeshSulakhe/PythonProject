
# write a function which takes list and int as input and returns the element at nth position in the list.
def get_n_element(lst:list,n:int):
    if 0 <= n < len(lst):
        return lst[n]
    else:
        return None

result = get_n_element([10,20,30,40,50],3)
print(result)