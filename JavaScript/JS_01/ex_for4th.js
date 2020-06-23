// 반복문

const numbers = [1,2,3,4,5]

for (number of numbers) {
  console.log(number)
}

// 위 반복문과 같은 결과가 나오는 코드?

// for (let i = 0; i < 5; i++) {
//   console.log(i)
// }

// for (const i = 1; i < 6; i++) {
//   console.log(i)
// }

// for (let i = 1; i < 6; i++){
//   console.log(i)
// }

// for (let i = 0; i of 5; i++) {
//   console.log(i)
// }


// 반복 & 조건문

let numbers = [1,2,3,4]
let odd = []
let even = []

// 결과 예측?

console.log(numbers)
for (number of numbers) {
  if (number % 2) {
    odd.push(number)
  } else {
    even.push(number)
  }
}
console.log([odd, even]) // [[1,3], [2,4]]

for (number in numbers) {
  if (number % 2) {
    odd.push(number)
  } else {
    even.push(number)
  }
}
console.log([odd, even]) // [['1','3'], ['0','2']]


// lodash library

let _ = require('lodash');
console.log(_.partition([1,2,3,4], n => n % 2))

const users = [
  {user: 'john', age: 20, active: true},
  {user: 'tak', age: 19, active: true},
  {user: 'neo', age: 30, active: false},
]

console.log(_.filter(users, 'active'))

console.log(_.uniq([2,0,2,0,0,7,1,6]))


// for -> forEach()

const items = ['a', 'b', 'c']
const copy = []

for (let i = 0; i < items.length; i++) {
  copy.push(items[i])
}

console.log(copy)

items.forEach(function(item) {
  copy.push(item)
})

console.log(copy)

items.forEach(item => copy.push(item))

console.log(copy)