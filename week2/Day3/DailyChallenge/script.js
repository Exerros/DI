// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by youself, without looking at the answers on the internet.


// let patern= "*"
// console.log(patern)
// for (let i=1; i<6 ; i++ ) {
//     patern = patern + "*"
//     console.log(patern)
// }


let patern= ""
console.log(patern)
for (let i=1; i<=6 ; i++ ) {
    for (let j=1; j<=i ; j++ ) {

        patern= patern + "*";
    }
    patern = patern + "\n";

}
    console.log(patern);




