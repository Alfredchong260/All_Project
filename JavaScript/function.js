function word(Noun, Adjective, Verb, Adverb)
{
    var result = "";
    result += "The" + " " + Adjective + " " + Noun + " " + Verb + " to the store " + Adverb;
    return result;
}

// console.log(word("dog", "big", "ran", "quickly"));
// console.log(word("bike", "slow", "flew", "slowly"));

function ReuseableFunction()
{
    console.log("Hello, World!");
}

// ReuseableFunction();

var Global = 10;
function fun1()
{
    // if include the var keyword the variable won't become global
    // but the variable can become global if without the var keyword
    // the pre-conditions will be the function has to used
    var oopsGlobal = 5;
    oopsGlobal = 5;
}
function fun2()
{
    var output = "";
    if(typeof Global != "undefined")
    {
        output = "Global : " + Global;
    }
    if(typeof oopsGlobal != "undefined")
    {
        output += "oopsGlobal : " + oopsGlobal;
    }
    console.log(output);
}

// fun1();
// fun2();

function LocalScope()
{
    var Var = 5;
    console.log(Var);
}

// LocalScope();


function OutFit()
{
    var Global = 100;

    return Global;
}

// console.log(OutFit());

function minus(num)
{
    return num - 7;
}

function multiply(num)
{
    return num * 5;
}

// console.log(minus(10));
// console.log(multiply(10));

function addThree()
{
    Global += 3;
}

console.log(addThree());
