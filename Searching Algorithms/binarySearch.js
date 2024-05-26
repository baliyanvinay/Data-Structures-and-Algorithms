// binary search - works for sorted array

const data = [4,8,12,21,33,55];


function binarySearch(data, lIndex, rIndex, searchItem) {
    if(lIndex > rIndex) { return -1 };

    const midIndex = Math.floor((lIndex+rIndex)/2);
    if(searchItem == data[midIndex]) { return midIndex };

    if(searchItem > data[midIndex]) {
        return binarySearch(data, midIndex+1, rIndex, searchItem);
    } else {
        return binarySearch(data, lIndex, midIndex, searchItem);
    }
}

console.info(binarySearch(data, 0, data.length-1, 12));