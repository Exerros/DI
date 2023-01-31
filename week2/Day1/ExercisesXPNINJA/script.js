// Exercise 1 : Evaluation
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

// Evaluate the comparisons found below:

    5 >= 1  //true
    0 === 1 //false
    4 <= 1 //false
    1 != 1 //false
    "A" > "B" //false
    "B" < "C"  //true
    "a" > "A"  //true
    "b" < "A" //false
    true === false //false
    true != true //false



// Exercise 2 : Ask For Numbers

// Instructions
// Ask the user for a string of numbers separated by commas
// Console.log the sum of the numbers.
// Hint: use some string methods
// Examples
// "2,3"➞ 5


let numbers= prompt("Enter a string of numbers separated by commas");
numbers= numbers.split(",");
console.log(numbers);
