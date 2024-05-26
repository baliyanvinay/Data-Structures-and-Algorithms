// counting sort

const data = [33,21,12,55,8,4];

function findMax(data) {
    let max = data[0];
    for(let i=1;i<data.length;i++) {
        if(data[i] > max) {
            max = data[i];
        }
    }
    return max;
}


function countingSort(data) {
    const maxElement = findMax(data); // 55

    // create array of maxElement+1 size with 0 as value
    const countArray = new Array(maxElement+1).fill(0);
    // [0,0,0 ... 0] 56 items in array with 0 as value

    for(let i=0;i<data.length;i++) {
        // increment the val at index in countArray of data item
        countArray[data[i]]++;
        // countArray[33] = 1;
        // countArray[21] = 1;
    }

    // commulative sum of countArray
    for(let i=1;i<countArray.length;i++) {
        countArray[i] = countArray[i] + countArray[i-1];
    }

    const output = new Array(data.length);
    for(let i=0;i<data.length;i++) {
        // for data item, get the value at its index
        // minus 1 that value
        // countArray[33]-1
        output[countArray[data[i]]-1] = data[i];
    }
    
    return output;
}

console.log(countingSort(data));