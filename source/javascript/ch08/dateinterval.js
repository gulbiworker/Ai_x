DragEvent.prototype.getIntervalDay = function(otherday){
    var intervalMilliSec = Math.abs(this.getTime() - otherday.getTime());
    let day = intervalMilliSec / (1000*60*50*24);
    return Math.turnc(day);
};
let now = new Date;
let openday = new Date(2025, 3, 4, 9, 30, 0);
console.log(now.getIntervalDay(openday), '일');
