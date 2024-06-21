function countLetters(arr) {
    var letters = [], counts = [], prev;

    for ( var i = 0; i < arr.length; i++ ) {
        if ( arr[i] !== prev ) {
            letters.push(arr[i]);
            counts.push(1);
        } else {
            counts[counts.length-1]++;
        }
        prev = arr[i];
    }

    var both = []
    letters.forEach((value, index) => {
        both.push({letter: value, count: counts[index]});
      });

    both = both.filter( (obj) => obj.count !== 1);
    return both;
}


var textArr = document.querySelector('pre').innerText.split('\n');
textArr.splice(textArr.length-1, 1);

var letterArrs = textArr.map((word) => [...word].sort());

var repeatsOnly = letterArrs.map( (letterArr) => countLetters(letterArr));

var components = [];
repeatsOnly.forEach((objArr) => {
    components.push(objArr.reduce((acc, cv) => {
        let twos   = cv.count === 2 ? 1 : 0;
        let threes = cv.count === 3 ? 1 : 0;
        return {dos: acc.dos + twos, tres: acc.tres + threes}
    }, {dos:0, tres:0}));
});

var summation = components.reduce((acc, cv) => {
    let twos   = cv.dos  ? 1 : 0;
    let threes = cv.tres ? 1 : 0;
    return {dos: acc.dos + twos, tres: acc.tres + threes};
}, {dos: 0, tres: 0});
console.log(summation);

var checksum = summation.dos * summation.tres;
console.log(checksum);

// 12217 is too high