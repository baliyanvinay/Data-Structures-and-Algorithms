// merge sort

const data = [33,21,12,55,8,4];


function copyArray(data, startIndex, endIndex) {
    const newArray = new Array(endIndex-startIndex);

    for(let i=0;i<newArray.length;i++) {
        newArray[i] = data[startIndex];
        startIndex++;
    }
    return newArray;
}


function merge(data, leftIndex, midIndex, rightIndex) {
    // make a copy of both left & right part
    
    const leftArray = copyArray(data, leftIndex, midIndex+1);
    const rightArray = copyArray(data, midIndex+1, rightIndex+1);

    let leftArrayIndex = 0;
    let rightArrayIndex = 0;
    let startIndex = leftIndex;

    // compare elements with left & right array & copy in data
    while(leftArrayIndex < leftArray.length && rightArrayIndex < rightArray.length) {
        
        if(leftArray[leftArrayIndex] < rightArray[rightArrayIndex]) {
            data[startIndex] = leftArray[leftArrayIndex];
            leftArrayIndex++;
        } else {
            data[startIndex] = rightArray[rightArrayIndex];
            rightArrayIndex++;
        }
        startIndex++;
    }

    // check if either left or right still has elements
    while(leftArrayIndex < leftArray.length) {
        data[startIndex] = leftArray[leftArrayIndex];
        leftArrayIndex++;
        startIndex++;
    }
    while(rightArrayIndex < rightArray.length) {
        data[startIndex] = rightArray[rightArrayIndex];
        rightArrayIndex++;
        startIndex++;
    }
}


function mergeSort(data, leftIndex, rightIndex) {
    if(leftIndex >= rightIndex) { return }

    const midIndex = Math.floor((leftIndex+rightIndex)/2);
    mergeSort(data, leftIndex, midIndex);
    mergeSort(data, midIndex+1, rightIndex);

    merge(data, leftIndex, midIndex, rightIndex);

}


mergeSort(data, 0, data.length-1);
console.log(data);