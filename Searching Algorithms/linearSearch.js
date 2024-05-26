// linear search

const data = [33,76,12,55,8,4];


function linearSearch(data, searchItem) {
    for(let i=0;i<data.length;i++) {
        if(searchItem == data[i]) {
            return i;
        }
    }
    return -1;
}

console.info(linearSearch(data, 12));