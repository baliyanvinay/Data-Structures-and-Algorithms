// bubble sort

const data = [33,21,12,55,8,4];


function bubbleSort(data) {
    let swapRequired;
    
    while(true) {
        swapRequired = false;

        for(let i=0;i<data.length-1;i++) {
            if(data[i]>data[i+1]) {
                [data[i], data[i+1]] = [data[i+1], data[i]];
                swapRequired = true;
    
            }
        }
        
        if(swapRequired == false) {
            break;
        }
    }
}

bubbleSort(data);
console.log(data);