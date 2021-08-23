function testingElse(val)
{
    if (val > 10){
        return "Bigger than 10";
    }
    else if (val < 5){
        return "Smaller than 5";
    }
   else{
        return "Between 5 and 10";
    }
}

function testSize(num)
{
    if (num < 5) {
        return "Tiny"
    }
    else if (num < 10) {
        return "Small"
    }
    else if (num < 15) {
        return "Medium"
    }
    else if (num < 20) {
        return "Large"
    }
    else {
        return "Huge"
    }

}


// console.log(testSize(19))

var names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"]
function golfScore(par, strokes)
{
    if (strokes == 1) {
        return names[0]
    }
    else if (strokes <= par -2) {
        return names[1]
    }
    else if (strokes == par -1) {
        return names[2]
    }
    else if (strokes == par) {
        return names[3]
    }
    else if (strokes = par + 1) {
        return names[4]
    }
    else if (strokes == par + 2) {
        return naems[5]
    }
    else if (strokes >= par + 3) {
        return names[6]
    }
}

// console.log(golfScore(4, 5));

function caseInSwitch(val)
{
    var answer = "";
    switch (val) {
        case 1:
            answer = "alpha";
            break;

        case 2:
            answer = "beta";
            break;

        case 3:
            answer = "gamma";
            break;

        case 4:
            answer = "delta";
            break;
    }
    return answer;
}

// console.log(caseInSwitch(4))

function switchOfStuff(val)
{
    var answer = "";
    switch (val) {
        case "a":
            answer = "apple";
            break;

        case "b":
            answer = "bird";
            break;

        case "c":
            answer = "cat";
            break;

        default:
            answer = "stuff";
            break;
    }
    return answer;
}

// console.log(switchOfStuff("t"))

function sequentialSizes(val)
{
    var answer = "";
    switch(val){
        case 1:
        case 2:
        case 3:
            answer = "Low";
            break;
        case 4:
        case 5:
        case 6:
            answer = "Mid";
            break;
        case 7:
        case 8:
        case 9:
            answer = "High";
            break;

    }
    return answer
}

// console.log(sequentialSizes(5))

function chainToSwitch(val)
{
    var answer = "";

    switch(val){
        case "bob":
            answer = "Marley";
            break;
        case 42:
            answer = "The Answer";
            break;
        case 1:
            answer = "There is no #1";
            break;
        case 99:
            answer = "Missed me by this much!"
            break;
        case 7:
            answer = "Ate Nine";
            break;
    }
    return answer
}

function isLess(a, b)
{
    if (a < b){
        return true;
    }
    else{
        return false;
    }
}

// console.log(isLess(20, 15))

function abTest(a, b)
{
    if (a < 0 || b < 0){
        return undefined;
    }

    return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
}

// console.log(abTest(-1, 16));

var count = 0;

function cc(card)
{
    switch(card)
        {
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            count ++;
            break;

        case 10:
        case "J":
        case "Q":
        case "K":
        case "A":
            count --;
            break;
        }

    var holdbet = "Hold";
    if (count > 0){
        holdbet = "Bet"
    }

    return count + " " + holdbet;
}

cc(2); cc("K"); cc(10); cc("K"); cc("A")
// console.log(cc(4))

var ourDog = {
    "name": "Caleb",
    "legs": 4,
    "tails": 1,
    "friends": ["everything!"]
}

var name = ourDog.name;
var dogName = ourDog["name"];

// console.log(name);
// console.log(dogName);

ourDog.bark = "bow-wow";
delete ourDog.tails;
// console.log(ourDog)


function phoneticLookup(val)
{
    var result = "";

    var lookup = {
        "alpha": "Adams",
        "bravo": "Boston",
        "charlie": "Chicago",
        "delta": "Denver",
        "echo": "Easy",
        "foxtrot": "Frank"
    }

    result = lookup[val];

    return result;
}

// console.log(phoneticLookup("charlie"))


var Object = {
    gift: "pony",
    pet: "kitten",
    bed: "sleigh"
};

function checkObj(checkProp)
{
    if (Object.hasOwnProperty(checkProp))
    {
        return Object[checkProp];
    }
    else{
        return "No Found"
    }
}

// console.log(checkObj("gift"))

var Music = [
    {
        "artist": "Billy Joel",
        "tile": "Piano Man",
        "release_year": 1973,
        "formats": [
            "CD",
            "8T",
            "LP"
        ],
        "gold": true
    },
    {
        "artist": "BlackPink",
        "tile": "How You Like That",
        "Release_year": 2019,
        "formats": [
            "YG Entertainment"
        ]
    }
]

var bios = Music[1].artist;
console.log(bios)

