// const fco = function(){
//   return n => n + 1
// }
// console.log(fco)

// const num_101 = fco()(100)
// console.log(num_101)

// const fco1 = function(n) {
//   return n + 1
// }
// console.log(fco1(100))

const numbersEach = function(numbers, callback){
  let acc
  for (const number of numbers){
    acc = callback(number, acc)
  }
  return acc
}
const addEach = (number, acc=0) => {
  return acc + number
}
const subEach = (number, acc=0) => {
  return acc - number
}
const mulEach = (number, acc=1) => {
  return acc * number
}

const NUMBERS = [1,2,3,4,5]
console.log(numbersEach(NUMBERS, addEach))
console.log(numbersEach(NUMBERS, subEach))
console.log(numbersEach(NUMBERS, mulEach))

console.log(numbersEach(NUMBERS, (number, acc = 0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc = 1) => acc * number))

const numbersAddEach = function(numbers){
  let sum = 0
  for (const number of numbers){
    sum += number
  }
  return sum
}
console.log(numbersAddEach([1,2,3,4,5]))

const numbersSubEach = function(numbers){
  let sum = 0
  for (const number of numbers){
    sum -= number
  }
  return sum
}
console.log(numbersSubEach([1,2,3,4,5]))

const numbersMulEach = function(numbers){
  let sum = 1
  for (const number of numbers){
    sum *= number
  }
  return sum
}
console.log(numbersMulEach([1,2,3,4,5]))