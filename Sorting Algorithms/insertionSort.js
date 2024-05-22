// insertion sort

const data = [33,21,12,55,8,4];


function insertionSort(data) {
    for(let i=1;i<data.length;i++) {
        // i starts at 1, since 1st item is considered sorted
        temp = data[i];

        let j = i-1;
        while(j>=0 && data[j]>temp) {
            data[j+1] = data[j]
            j--;
        }
        data[j+1]=temp; //j+1 because of j-- at line 14
    }
}

insertionSort(data);
console.log(data);