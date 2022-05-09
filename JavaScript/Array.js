// Array
// Can either create a variable to store the info or straightly print out the info
var Array = ["John", 10, "15", "Cat"];
console.log(Array[1]);
var myArray = [["Boolean", 10], ["Variable", 100], ["Node", 10]];

// Modify data with index
Array[0] = "Ali"
Array[1] = 100;
console.log(Array);

// Access multi dimension Array
console.log(myArray[0][1]);

// Add more info to Array by push()
Array.push("Catherine", "Johnson");
console.log(Array);

// Delete last info from Array by pop()
Array.pop();
console.log(Array);

// Delete first info from Array by shift()
Array.shift();
console.log(Array);

// Undo the delete for first info by replace a new info by unshift()
Array.unshift("Happy");
console.log(Array);

