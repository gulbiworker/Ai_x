/* 변수 선언시 var 전역변수   let 지역변수 */
sum = 0;
for(var i=1 ; i<=5 ; i++){
    sum += i; 
}

console.log('for문 끝')
console.log('i=', i, '일때까지 누적합은', sum);


