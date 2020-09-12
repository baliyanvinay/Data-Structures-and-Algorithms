# Bubble Sort compares first element to second and swap them if order does not fit.
array_elements = [12, 17, 18, 29, 30]

#Two loops are required: one to run until array is fully sorted and another to check and swap elements
unsorted_flg = True
while(unsorted_flg):
    unsorted_flg=False
    for i in range(len(array_elements)-1):
        if(array_elements[i] > array_elements[i+1]):
            array_elements[i], array_elements[i+1] = array_elements[i+1], array_elements[i]
            unsorted_flg=True # to keep the while loop ongoing

print(array_elements, sep=' ')