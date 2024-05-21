// selection sort

const data = [33,21,12,55,8,4];

function selectionSort(data) {
    let minimum;
    let index;
    for(let i=0;i<data.length-1;i++) {
        minimum = data[i];
        index = i;
        for(let j=i+1;j<data.length;j++) {
            if(minimum>data[j]) {
                minimum = data[j];
                index = j;
            }
        }
        if(index != i) {
            [data[i], data[index]] = [data[index], data[i]];
        }
    }
}

selectionSort(data);
console.log(data);