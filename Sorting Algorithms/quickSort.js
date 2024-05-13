// quick sort

function swapItems(list, index1, index2) {
    let temp = list[index1];
    list[index1] = list[index2];
    list[index2] = temp;
}

function quickSort(list, startIndex, endIndex) {

    if(startIndex >= endIndex) {
        return
    }

    let pivot = list[endIndex];
    let swapPointer = startIndex;
    let movePointer = startIndex;

    while(movePointer < endIndex) {
        if(list[movePointer]<pivot) {
            swapItems(list, movePointer, swapPointer);
            swapPointer++;
        }
        movePointer++;
    }
    swapItems(list, swapPointer, endIndex);

    quickSort(list, startIndex, swapPointer-1);
    quickSort(list, swapPointer+1, endIndex);
}
