function pow(x=1, y=2){
    var result = 1;
    for(let cnt=1 ; cnt<=y ; cnt++){
        result *= x;
    }
    return result;
}
console.log(pow(3,3));

function pow(x=1, y=2){
    let result = 1;
    for(let cnt=1 ; cnt<=y ; cnt++){
        result *= x;
    }
    return result;
}