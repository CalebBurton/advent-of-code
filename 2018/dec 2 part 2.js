function arrCheck(words) {
    var diff = 0;
    for (var j = 0; j < Math.ceil(words.length / 2); j++) {
        for (var i = 0; i < words.length; i++) {
            if (i !== j) {
                diff = letterDistance(words[j], words[i])
                if (diff === 1) {
                    console.log(`Found: indices ${i} and ${j}`)
                    return i, j;
                }
            }
        }
    }
}


function letterDistance (word1, word2) {
    var arr1 = [...word1];
    var arr2 = [...word2];
    var diff = 0;

    arr1.forEach( (letter, index) => {
        if(arr2[index] !== letter) {
            diff++;
        }
    });
    return diff;
}


var textArr = document.querySelector('pre').innerText.split('\n');
textArr.splice(textArr.length-1, 1);

// pebjqsalrdnckzfihvtxysomg
// pebjqsalrdnckzfihvtxysomg