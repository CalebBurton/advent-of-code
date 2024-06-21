const textArr = document.querySelector('pre').innerText.split('\n');
textArr.splice(textArr.length-1, 1);

const instructionArr = textArr.map((text) => {
    let [,,xstart,ystart,,xlength,ylength] = text.split(/[,:x ]/);
    [xstart, ystart, xlength, ylength] = [parseInt(xstart,10), parseInt(ystart,10), parseInt(xlength,10), parseInt(ylength,10)];
    const xend = xstart + xlength;
    const yend = ystart + ylength;
    return {xstart, xend, ystart, yend};
});

const gridSize = instructionArr.reduce((acc, cv) => {
    acc.xmin = cv.xstart < acc.xmin ? cv.xstart : acc.xmin;
    acc.xmax =   cv.xend > acc.xmax ?   cv.xend : acc.xmax;

    acc.ymin = cv.ystart < acc.ymin ? cv.ystart : acc.ymin;
    acc.ymax =   cv.yend > acc.ymax ?   cv.yend : acc.ymax;

    return acc;
}, {xmin: 0, xmax: 0, ymin: 0, ymax: 0});

let grid = Array.from({length: gridSize.ymax}, () => Array.from({length: gridSize.xmax}, () => 0));

instructionArr.forEach((instruction) => {
    for (let i = instruction.ystart; i < instruction.yend; i++) {
        for (let j = instruction.xstart; j < instruction.xend; j++) {
            grid[i][j] += 1;
        }
    }
});

const multipleClaims = grid.reduce((rowAcc,row) => rowAcc + row.reduce((cellAcc, cell) => cell > 1 ? cellAcc + 1 : cellAcc, 0), 0);
console.log(multipleClaims);

// 119551