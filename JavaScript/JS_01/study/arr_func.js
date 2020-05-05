var numberArray = [1,2,3,4,5,6,7,8,9];
var spliceArray = numberArray.splice(4, 5);

console.log(spliceArray.join(', '))
console.log(numberArray.join(', '))
console.log(numberArray[4])
console.log(numberArray[5])
// console.log(numberArray[6])
// console.log(numberArray[7])

// document.writeln("<p>" + spliceArray.join(', ') + "</p>");
// document.writeln("<p>" + numberArray.join(', ') + "</p>");
// document.writeln("<p>" + numberArray[5] + "</p>");