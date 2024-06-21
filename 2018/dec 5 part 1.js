const fullText = document.querySelector('pre').innerText.split('\n')[0];
// const fullText = 'dabAcCaCBAcCcaDA';
const textArr = [...fullText];

var lengths = [];

function recur(arr, failsafe = 0) {
    console.log(`Recursion level ${failsafe}`);
    failsafe++;
    var workingArr = [];
    for (let i = 0; i < arr.length - 1; i++) {
        var current = arr[i];
        var next = arr[i+1];

        var Aa = current.toUpperCase() === next;
        var aA = next.toUpperCase() === current;

        if ((current !== next) && (Aa || aA)) {
            i++;
        } else {
            workingArr.push(current);
            if (i === arr.length - 2) {
                workingArr.push(next);
            }
        }
    }
    lengths.push(workingArr.join('').length)
    console.log(`\t\t${lengths[lengths.length - 1]}`);
    // console.log(`\t\t${arr.join('')}\n\t\t${workingArr.join('')}`);
    if ((workingArr.join('') !== arr.join('')) && (failsafe < 1000)) {
        return recur(workingArr, failsafe);
    } else {
        console.log('returning...');
        return workingArr;
    }
}

var result = recur(textArr.slice());
console.log('\n----------------------------------');
console.log(result.length)
// console.log(result === 'dabCBAcaDA');
// console.log(`Received: ${result}`);
// console.log(`Expected: dabCBAcaDA`);

// 10  => 12254
// 20  => 12234
// 50  => 12174
// 300 => 11674
// 735 => 10804