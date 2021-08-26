function randomFraction()
{
    var randomNum = Math.floor(Math.random() * 10);
    return randomNum;
}

// console.log(randomFraction())

function randomRange(min, max)
{
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// console.log(randomRange(1, 9))

function convertToInt(str)
{
    return parseInt(str)
}
// console.log(convertToInt("40"))

function conToInt(str)
{
    return parseInt(str, 2)
}

// console.log(conToInt("10011"))

function checkEqual(a, b)
{
    return a === b ? true : false
}

// console.log(checkEqual(10, 10))

function checkSign(num)
{
    return num > 0 ? "Positive" : num < 0 ? "Negative" : "Zero"
}

// console.log(checkSign(120))

let catName = "Moko";
let quote;

catName = "Beau";

function catTalk()
{
    "use strict";

    catName = "Oliver";
    quote = catName + "say Meows";
}

function printManyTimes(str)
{
    "use strict";
    
    const SENTENCE = str + " is cool!";


    for(let i = 0; i < str.length; i += 2)
        console.log(SENTENCE)
}

// printManyTimes("haiyaaaaaa")

const s = [5, 7, 2];
function editInPlace()
{
    "use strict";

    s[0] = 2;
    s[1] = 5;
    s[2] = 7;

}
// editInPlace()
// console.log(s)

function freezeObj()
{
    const MATH_CONSTANTS = {
        PI : 3.14
    };

    Object.freeze(MATH_CONSTANTS);

    try
    {
        MATH_CONSTANTS.PI = 99;
    }
    catch( ex )
    {
        console.log(ex);
    }
    return MATH_CONSTANTS.PI;
}

const PI = freezeObj();

// console.log(PI)


const magic = (arr1, arr2) => arr1.concat(arr2);

// console.log(magic([1, 2], [3, 4, 5]));

const realNumberArray = [4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2]

const squareList = (arr) => {
    const squaredIntegers = arr.filter(num => Number.isInteger(num) && num > 0).map(x => x * x);
    return squaredIntegers;
};

const squaredIntegers = squareList(realNumberArray);
console.log(squaredIntegers);
