function sumAll(){
// 매개변수가 없으면 -999 return
// 매개변수가 있으면 매개변수들의 합을 return
if(arguments.length==0){
    return(-999);
}else if(arguments.length>=1){
    let total = 0;
    for(let num of arguments){
        
        total +=num;  
    }return total;

}
}

// test
console.log(sumAll());
console.log(sumAll(1,2));
console.log(sumAll(1,2,3,4,5));