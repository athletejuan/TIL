function numbersAddEach(numbers){
  let sum = 0
  for (const number of numbers){
    sum += number
  }
  return sum
}
console.log(numbersAddEach([1,2,3,4,5]))

const NUMBERS = [1,2,3,4,5]

function numbersEach(numbers, callback){
  let acc
  for (const number of numbers){
    acc = callback(number, acc)
  }
  return acc
}

function addEach(number, acc=0){
  return acc += number
}

console.log(numbersEach(NUMBERS, addEach))
console.log(numbersEach(NUMBERS, (number, acc=0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc=0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc=1) => acc * number))