function recur(numArr, level = 0) {
  console.log(`recurring at level ${level}`);
  var na = numArr.concat(numArr);
  var rt = [];
  na.reduce(function(a,b,i) { return rt[i] = a+b; },0);
  var found = findRepeats(rt, repeatedNums);
  if (found) {
    return na, rt, found;
  } else {
    level++
    recur(na, level);
  }
}


function findRepeats (runningTotal, repeatedNums) {
  repeatedNums = [];

  runningTotal.forEach((el, ind) => {
    var next = runningTotal.indexOf(el, ind + 1);
    if(next !== -1) {
      var outie = {val: el, ind: runningTotal.indexOf(el, ind + 1)};
      repeatedNums.push(outie)
    }
  });

  if(repeatedNums.length) {
    console.table(repeatedNums);
    return repeatedNums;
  } else {
    return false;
  }
}


var textArr = document.querySelector('pre').innerText.split('\n');

var numArr = textArr.map((s) => parseInt(s,10));
numArr.splice(numArr.length-1, 1);

var runningTotal = [];
numArr.reduce(function(a,b,i) { return runningTotal[i] = a+b; },0);

var repeatedNums = [];


var na2 = numArr.concat(numArr);
var na3 = na2.concat(na2);
var na4 = na3.concat(na3);
var na5 = na4.concat(na4);
var na6 = na5.concat(na5);
var na7 = na6.concat(na6);
var na8 = na7.concat(na7);
var na9 = na8.concat(na8);
var rt9 = [];
na9.reduce(function(a,b,i) { return rt9[i] = a+b; },0);





//---------------------------------------------------




repeatedNums = findRepeats(rt9, repeatedNums);




//---------------------------------------------------




var found = false;
var max = 137000;
var ind = 135800;
while (!found && ind < max) {
  found = repeatedNums.find(x => x.ind === ind);
  if (ind % 1000 === 0){
    console.log(`cycle ${ind} of ${max}`);
  }
  ind++;
}

if (found) {
  console.log(found);
}