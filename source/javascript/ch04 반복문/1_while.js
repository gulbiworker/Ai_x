// while(조건){반복할 명령어들;} do{반복할 명령어들;} while(조건); 1초동안 while 문을 몇번 실행했는지 출력
var now = new Date();
var startTime = now.getTime();
//console.log(startTime);
while(new Date().getTime() < startTime + 1000){
    cnt++;
}
console.log(cnt);
startTime = new Data().getTime();
cnt=0;
do{
    ++cnt;
}while(new Date().getTime < startTime +1000);
console.log(cnt)