# Selection Sort
array_list=list(map(int, input('Enter the elements of arrays: ').split()))

# Selection sort divides the array into two parts: sorted and unsorted
for i, element in enumerate(array_list):
    # finding the minimum of the array_list
    min_element=element
    for el in array_list[i:]:
        if min_element>el:
            min_element=el
            index=array_list.index(el)
    if min_element!=element:
        array_list[i], array_list[index]=array_list[index], array_list[i]
    
print(array_list, sep=' ')
