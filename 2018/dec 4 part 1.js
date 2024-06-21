const textArr = document.querySelector('pre').innerText.split('\n');
textArr.splice(textArr.length-1, 1);
textArr.sort();

var logs = textArr.map((text) => {
    let [,,month,day,hour,min,,trigger,,potentialNum] = text.split(/[\s\[\]#:-]/);
    [month,day,hour,min] = [parseInt(month,10),parseInt(day,10),parseInt(hour,10),parseInt(min,10)];
    let status = '';
    let guardNum = -1;
    switch (trigger) {
        case "falls":
            status = 'asleep';
            break;
        case "wakes":
            status = 'awake';
            break;
        case "Guard":
            guardNum = parseInt(potentialNum,10);
            status = 'awake';
            break;
        default:
            console.error('UNEXPECTED TRIGGER WORD');
            break;
    }
    return {month, day, hour, min, guardNum, status}
});

logs.forEach((log, ind) => {
    if (log.guardNum === -1) {
        logs[ind].guardNum = logs[ind - 1].guardNum;
    }
});

var extrapolated = [logs[0]];
for (let ind = 1; ind < logs.length; ind++) {
    const oLog = logs[ind - 1];
    const oTime = new Date(1518,oLog.month,oLog.day,oLog.hour,oLog.min);
    const nLog = logs[ind];
    const nTime = new Date(1518,nLog.month,nLog.day,nLog.hour,nLog.min);
    const diff = ((nTime - oTime) / 1000) / 60;
    for (let extraMins = 1; extraMins < diff; extraMins++) {
        let eTime = new Date(oTime);
        eTime.setMinutes( eTime.getMinutes() + extraMins );
        extrapolated.push(
            {
                month: eTime.getMonth(),
                day: eTime.getDate(),
                hour: eTime.getHours(),
                min: eTime.getMinutes(),
                guardNum: oLog.guardNum,
                status: oLog.status
            }
        );
    }
    extrapolated.push(nLog);
}

var allGuards = [];
logs.forEach( (log) => {
    let newGuard = !Boolean(allGuards.find((guard) => guard === log.guardNum));
    if (newGuard) {
        allGuards.push(log.guardNum);
    }
});
allGuards.sort((a, b) => a - b);
console.log(allGuards);

/*
var giantClock =
[ // hour
    [ // minute
        { // log
            $guardNum: [
                {month: 3, day: 5, status: 'awake'}
            ]
        }
    ],
];
*/

var giantClock = [];
for (let h = 0; h < 24; h++) {
    giantClock.push([]);
    for (let m = 0; m < 60; m++) {
        giantClock[h].push({});
    }
}

extrapolated.forEach( (item) => {
    const newObj = {month: item.month, day: item.day, status: item.status};
    if(!giantClock[item.hour][item.min][`${item.guardNum}`]) {
        giantClock[item.hour][item.min][`${item.guardNum}`] = [newObj];
    } else {
        giantClock[item.hour][item.min][`${item.guardNum}`].push(newObj);
    }
});

var totalSleeps = [];
allGuards.forEach( (g) => {
    let totalSleep = 0;
    for (let h = 0; h < 24; h++) {
        for (let m = 0; m < 60; m++) {
            // if (h===23 && m===58 && g===97) {
            //     let aa  = giantClock[h][m][`${g}`][0].status;
            //     let aaa = giantClock[h][m][`${g}`].reduce((acc, val) => { return val.status === 'awake' ? acc + 1 : acc }, 0);
            //     console.log(`\n\n------------------\n${aa}\n${aaa}\n------------------\n\n`);
            // }
            totalSleep += giantClock[h][m][`${g}`].reduce((acc, val) => { return val.status === 'asleep' ? acc + 1 : acc }, 0)
        }
    }
    let ob = {
        guardNum: g,
        totalSleep: totalSleep
    };
    totalSleeps.push(ob);
})

totalSleeps.sort((a,b) => b.totalSleep - a.totalSleep)
// console.log(totalSleeps[0])

// GUARD NUMBER 2851 * MINUTE NUMBER 44 = 125444

var clock2851 = [];
for (let h = 0; h < 24; h++) {
    clock2851.push([]);
    for (let m = 0; m < 60; m++) {
        clock2851[h].push({});
    }
}

extrapolated.forEach( (item) => {
    if (item.guardNum === 2851) {
        const newObj = {month: item.month, day: item.day, status: item.status};
        if(!clock2851[item.hour][item.min][`2851`]) {
            clock2851[item.hour][item.min][`2851`] = [newObj];
        } else {
            clock2851[item.hour][item.min][`2851`].push(newObj);
        }
    }
});


for (let h = 0; h < 24; h++) {
    for (let m = 0; m < 60; m++) {
        clock2851[h][m] = clock2851[h][m][`2851`].reduce((acc, val) => { return val.status === 'asleep' ? acc + 1 : acc }, 0)
    }
}

var highestHour;
var [globalMax, localMax] = [0,0];
for (let h = 0; h < 24; h++) {
    localMax = clock2851[h].reduce((acc, val) => { return val > acc ? val : acc }, 0)
    if (globalMax < localMax) {
        globalMax = localMax;
        highestHour = h;
    }
}
var freqOfMostFrequent   = clock2851[highestHour].reduce((acc, val) => val > acc ? val : acc, 0)
var minuteOfMostFrequent = clock2851[highestHour].findIndex((x) => x >= freqOfMostFrequent); 

console.log(minuteOfMostFrequent)