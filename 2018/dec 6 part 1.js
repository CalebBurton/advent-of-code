var textArr = document.querySelector('pre').innerText.split('\n');
textArr.splice(textArr.length-1, 1);
textArr = textArr.map((str) => {
    var coords = str.split(', ')
    return [parseInt(coords[0],10), parseInt(coords[1],10)];
});

// var textArr = [
//     [1, 1],
//     [1, 6],
//     [8, 3],
//     [3, 4],
//     [5, 5],
//     [8, 9]
// ];

var xEdge = textArr.slice().sort((a,b) => a[0] - b[0]);
var yEdge = textArr.slice().sort((a,b) => a[1] - b[1]);

xEdge = xEdge.filter((pair) => ((pair[0] === xEdge[0][0]) || (pair[0] === xEdge[xEdge.length - 1][0])));
yEdge = yEdge.filter((pair) => ((pair[1] === yEdge[0][1]) || (pair[1] === yEdge[yEdge.length - 1][1])));

var finite = textArr.filter((pair) => {
    const notXMin = (pair[0] !== xEdge[xEdge.length - 1][0]);
    const notXMax = (pair[0] !== xEdge[0][0])
    const notYMin = (pair[1] !== yEdge[yEdge.length - 1][1]);
    const notYMax = (pair[1] !== yEdge[0][1])
    return (notXMin && notXMax && notYMin && notYMax);
});


console.log(xEdge)
console.log(yEdge)
console.log(finite)

// Can't solve. Requires algorithmic approach, graph theory, something of the sort that I've never learned.