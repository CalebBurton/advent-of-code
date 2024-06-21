const fullText = document.querySelector('pre').innerText.split('\n')[0];
const textArr = [...fullText];

// var fullText = 'dabAcCaCBAcCcaDA';
// var textArr = [...fullText];

function recur(arr, failsafe = 0) {
    // console.log(`Recursion level ${failsafe}`);
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
    // lengths.push(workingArr.join('').length)
    // console.log(`\t\t${lengths[lengths.length - 1]}`);
    // console.log(`\t\t${arr.join('')}\n\t\t${workingArr.join('')}`);
    if ((workingArr.join('') !== arr.join(''))/*  && (failsafe < 2000) */) {
        return recur(workingArr, failsafe);
    } else {
        console.log('returning...');
        return workingArr.join('');
    }
}



// var result = recur(textArr.slice());
// console.log('\n----------------------------------');
// console.log(result.length)

// 10  => 12254
// 20  => 12234
// 50  => 12174
// 300 => 11674
// 735 => 10804

//---------------------------------------------------------------------------------------------
//---------------------------------------------------------------------------------------------
//---------------------------------------------------------------------------------------------

function remove(letter, arr) {
    var workingArr = [];
    for (let i = 0; i < arr.length; i++) {
        var current = arr[i];
        if (current.toUpperCase() !== letter.toUpperCase()) {
            workingArr.push(current);
        }
    }
    return workingArr;
}


// var res_a = remove('a', textArr);
// var res_b = remove('b', textArr);
// var res_c = remove('c', textArr);
// var res_d = remove('d', textArr);

// var react_a = recur(res_a);
// var react_b = recur(res_b);
// var react_c = recur(res_c);
// var react_d = recur(res_d);

// console.table([
//     {letter: 'a', rem: res_a, e_rem: 'dbcCCBcCcD',     rem_len: res_a.length, react: react_a, react_len: react_a.length, e_react_len: 6},
//     {letter: 'b', rem: res_b, e_rem: 'daAcCaCAcCcaDA', rem_len: res_b.length, react: react_b, react_len: react_b.length, e_react_len: 8},
//     {letter: 'c', rem: res_c, e_rem: 'dabAaBAaDA',     rem_len: res_c.length, react: react_c, react_len: react_c.length, e_react_len: 4},
//     {letter: 'd', rem: res_d, e_rem: 'abAcCaCBAcCcaA', rem_len: res_d.length, react: react_d, react_len: react_d.length, e_react_len: 6}
// ])




// -------------------------------------------------------------------------
// -------------------------------------------------------------------------
// -------------------------------------------------------------------------


var alphabet = 'abcdefghijklmnopqrstuvwxyz1'.split('');
var finalTable = [];

alphabet.forEach((letter) => {
    var reduced = remove(letter, textArr);
    var reacted = recur(reduced);
    finalTable.push(
        {
            letter: letter,
            reduced: reduced.length,
            reacted: reacted.length
        }
    );
})

finalTable.sort((a,b) => a.reacted - b.reacted)


// 9781 is too high
// 6649 is too low

// 6650 is right...not sure why