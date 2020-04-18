const numbersAddEach = numbers => {
  let sum = 0
  for (const number of numbers){
    sum += number
  }
  return sum
}
console.log(numbersAddEach([1,2,3,4,5]))

const numbersSubEach = numbers => {
  let sum = 0
  for (const number of numbers){
  sum -= number
  }
  return sum
}
console.log(numbersSubEach([1,2,3,4,5]))

const numbersMulEach = numbers => {
  let sum = 1
  for (const number of numbers){
    sum *= number
  }
  return sum
}
console.log(numbersMulEach([1,2,3,4,5]))

const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers){
    acc = callback(number, acc)
  }
  return acc
}

// 배열합
const addEach = function(number, acc = 0){
  return acc + number
}
//배열차
const subEach = (number, acc = 0) => {
  return acc - number
}
//배열곱
const mulEach = (number, acc = 1) => {
  return acc * number
}

console.log(numbersEach([1,2,3,4,5], mulEach))

NUMBERS = [1,2,3,4,5]
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc = 1) => acc * number))