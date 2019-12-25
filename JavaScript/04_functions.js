// 선언식(statement, declaration)
function add(num1, num2){
    return num1 + num2
}

// console.log(add(2,7)) // 9

// 표현식(expression)
const sub = function(num1, num2){
    return num1 - num2
}

// console.log(sub(7,2)) // 5

// 기본인자(Default Args)

const greeting = function(name='noName'){
    console.log(`hi ${name}`)
}

console.log(typeof add)
console.log(typeof sub)
console.log(greeting)


// Hoisting

add(2,7) // 9

function add(num1, num2){
    return num1 + num2
}

// Hoisting (x)
// sub(7,2) // Uncaught ReferenceError

// const sub = function(num1, num2){
//     return num1 - num2
// }

// var sub = function(num1, num2){
//     return num1 - num2
// }

// Arrow Function

const arrow = function(name){
    return `hello! ${name}`
}

// 1. function 키워드 삭제
// const arrow = (name) => { return `hello! ${name}`}

// 2. () 생략 (함수 매개변수가 하나일 경우만)
// const arrow = name => { return `hello! ${name}`}

// 3. {} & return 생략 (바디가 표현식 1개)
// const arrow = name => `hello! ${name}`

// Arrow function refactoring
// 1. arrow function
square = (num) => { return num ** 2 }

// 2. 인자가 한개면 ()도 생략가능
// square = num => { return num ** 2 }

// 3. 함수의 body가 한줄이면 {}와 return키워드도 생략 가능
// square = num => num ** 2

// 4. 인자가 없다면? () of _ 로 표시 가능
let noArgs = () => 'No args'
noArgs = _ => 'No args'

// 5-1. object를 return 한다면
let returnObject = () => { return {key: 'valur'} } // return을 명시적으로 적어야 함

// 5-2. return을 적지않으면 괄호를 붙여야 한다
returnObject = () => ({ key: 'value' })

// IIFE(Immediately Invoked Function Expression)
(function (num) { return num ** 3})(2) // 8

(num => num ** 0.5)(4) // 2