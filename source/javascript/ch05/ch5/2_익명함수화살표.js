let funVar = function(){
  console.log('1. 매개변수 없는 일반 함수 호출');
}
funVar();
funVar = ()=>{
  console.log('2. 매개변수 없는 화살표 함수 호출');
}
funVar();
funVar = function(i){
  console.log('3. 매개변수가 하나 있는 일반 함수 호출');
  console.log('매개변수 값 = ', i);
}
funVar(10);
funVar = i=>{
  console.log('4. 매개변수가 하나 있는 화살표 함수 호출');
  console.log('매개변수 값 = ', i);
}
funVar(10);
funVar = function(i){
  console.log('5. 매개변수가 하나의 한줄짜리 일반 함수 호출', i);
}
funVar(20);
funVar = function(x){
    return x*x;
}
console.log(funVar(10));
funVar = x => x*x
console.log(funVar(7));

funVar = (x,y) => 10*x+y;
console.log(funVar(5,3));

var arr=[10,'홍길동','신림동'];
arr.forEach((data, idx) => console.log(idx, data);)
