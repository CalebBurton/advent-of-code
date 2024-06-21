var textArr = document.querySelector('pre').innerText.split('\n');

// var textArr = `Step C must be finished before step A can begin.
// Step A must be finished before step D can begin.
// Step F must be finished before step E can begin.
// Step D must be finished before step E can begin.
// Step B must be finished before step E can begin.
// Step A must be finished before step B can begin.
// Step C must be finished before step F can begin.
// `.split('\n');

textArr.splice(textArr.length-1, 1);
textArr.sort();
textArr = textArr.map((str) => [str.substr(5,1), str.substr(36,1)]);
var allLetters = [];
textArr.forEach((pair) => {
    if (allLetters.indexOf(pair[0]) === -1) {
        allLetters.push(pair[0]);
    }
    if (allLetters.indexOf(pair[1]) === -1) {
        allLetters.push(pair[1]);
    }
});
allLetters.sort();

function findBlocking(target) {
    return textArr.filter((pair)=> pair[1] === target).map((pair) => pair[0]);
}
function findBlockedBy(target) {
    return textArr.filter((pair)=> pair[0] === target).map((pair) => pair[1]);
}

var objArr = [];
allLetters.forEach((letter) => objArr.push({letter: letter, blockedBy: findBlocking(letter), blocking: findBlockedBy(letter)}));
objArr = objArr.filter((val, i, arr) => (i !== 0) ? ((val.letter !== arr[i-1].letter) && (val.blocking !== arr[i-1].blocking)) : true);

var bigOb = {};
objArr.forEach((ob) => {
    bigOb[ob.letter] = {blocking: ob.blocking, blockedBy: ob.blockedBy};
});

var start = allLetters.filter((l) => bigOb[l].blockedBy.length === 0)[0];

var sequence = [];
var options = [];
var lastLetter = start;
var i = 0;
while ((sequence.length < allLetters.length) && (lastLetter && lastLetter.length) && (i < 500)) {
    // debugger;
    sequence.push(lastLetter);
    var lessBlocked = bigOb[lastLetter].blocking;
    var unBlocked = lessBlocked.filter((l) => {
        var noBlocksYet = true;
        var allBlocks = bigOb[l].blockedBy;
        // console.log(`--------- ${l} -------------`)
        for (var a = 0; a < allBlocks.length; a++) {
            var bl = allBlocks[a]
            // console.log({letter: bl, and1: noBlocksYet, and2: (sequence.indexOf(bl) !== -1), total: (noBlocksYet && (sequence.indexOf(bl) !== -1))});
            noBlocksYet = noBlocksYet && (sequence.indexOf(bl) !== -1);
        };
        return noBlocksYet;
    });
    options = Array.concat(options, unBlocked);
    options.sort();
    lastLetter = options.shift();
    i++;
}
console.log(`----- FINAL SEQUENCE -----`)
console.log(sequence);



// Gave up after 3 hours