// 논리연산자 우선순위 & NOT!
console.log(true || false && false)      // returns true, because && is executed first
console.log((true || false) && false)    // returns false, because operator precedence cannot apply
console.log((true || false) && !false)   // returns true


// 삼항연산자
const age = 23;
const canDrinkAlcohol = (age > 19) ? "True, over 19" : "False, under 19";
console.log(canDrinkAlcohol); // "True, over 19"

// 반복문

const numbers = [1,2,3,4,5]

for (number of numbers) {
  console.log(number)
}

// 위 반복문과 같은 결과가 나오는 코드?

for (let i = 0; i < 5; i++) {
  console.log(i)
}

for (const i = 1; i < 6; i++) {
  console.log(i)
}

for (let i = 1; i < 6; i++){
  console.log(i)
}

for (let i = 0; i of 5; i++) {
  console.log(i)
}


// 반복 & 조건문

const numbers = [1,2,3,4]
const odd = []
const even = []

// for of
console.log(numbers)
for (number of numbers) {
  if (number % 2) {
    odd.push(number)
  } else {
    even.push(number)
  }
}
console.log([odd, even]) // [[1, 3], [2, 4]]

// for in
for (number in numbers) {
  if (number % 2) {
    odd.push(number)
  } else {
    even.push(number)
  }
}
console.log([odd, even]) // [['1', '3'], ['0', '2']]


// lodash library

let _ = require('lodash');
console.log(_.partition([1,2,3,4], n => n % 2))

const users = [
  {name: 'john', age: 20, active: true},
  {name: 'tak', age: 19, active: true},
  {name: 'neo', age: 30, active: false},
]

console.log(_.filter(users, 'active'))

console.log(_.uniq([2,0,2,0,0,7,1,6]))

console.log(_.sortBy(_.sampleSize(_.range(1,46), 6)))


// forEach

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


// arrow function

items.forEach(item => copy.push(item))

console.log(copy)

// map

const users = [
  {name: 'john', age: 20, active: true},
  {name: 'tak', age: 19, active: true},
  {name: 'neo', age: 30, active: false},
]
const user_names = users.map(user => user.name)
console.log(user_names)

// filter

const targetUser = users.filter(user => 
  user.age > 19 && user.active
)
console.log(targetUser)