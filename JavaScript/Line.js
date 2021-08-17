function nextInLine(arr, item)
{
    arr.push(item);
    return arr.shift();
}

var testArr = [1, 2, 3, 4, 5];

// console.log("Before: " + JSON.stringify(testArr));
// console.log(nextInLine(testArr, 6));
// console.log("After: " + JSON.stringify(testArr));

// Boolean
function Booleans(isTrue)
{
    if (isTrue)
    {
        return "Yes. it's true";
    }
    return "No. it's false";
}

function trueOrFlase(wasthatTrue)
{
    if (wasthatTrue)
    {
        return "Yes, that was true";
    }
    return "No, that was false";
}

// console.log(trueOrFlase(true))

// Camparison
function testEqual(val)
{
    if (val == '7')
    {
        return "Equal";
    }
    return "Not Equal";
}

// console.log(testEqual(7));

/*
== will consider 7 != "7"
=== will consider 7 == "7"
*/

function LogicalTest(val)
{
    if (val => 25 && val <= 50)
    {
        return "Between 25 and 50";
    }
    if (val < 25)
    {
        return "Less than 25";
    }
    else 
    {
        return "More than 50";
    }
}

console.log(LogicalTest(50.5));
