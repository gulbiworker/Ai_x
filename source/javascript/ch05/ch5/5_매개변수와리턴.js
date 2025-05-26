console.log(pow(5,3));

console.log(pow(5,3,12,10)); // 많으면 뒷부분 무시  적으면 undefined
function pow(x, y){
    let result = 1;
    for(let cnt=1 ; cnt<=y ; cnt++){
        result *= x;
    }
    return result;
}