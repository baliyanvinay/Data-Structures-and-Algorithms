# Bubble Sort compares first element to second and swap them if order does not fit.
array_elements = [52, 17, 28, 79, 30]

#Two loops are required: one to run until array is fully sorted and another to check and swap elements
unsorted_flg = True
round=0
while(unsorted_flg):
    unsorted_flg=False
    round+=1
    print(f'\nSorting Round {round}')
    for i in range(len(array_elements)-1):
        print(f'Sorting Step {i+1}: {array_elements}', sep=' ')
        if(array_elements[i] > array_elements[i+1]):
            array_elements[i], array_elements[i+1] = array_elements[i+1], array_elements[i]
            unsorted_flg=True # to keep the while loop ongoing

print(f'\nSorted List: {array_elements}', sep=' ')