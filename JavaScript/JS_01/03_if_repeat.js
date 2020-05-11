// var readline = require('readline')

// var userName = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// })

// userName.question('', answer => {
//     console.log(answer)
//     userName.close();
// })

const userName = 'ssafy'

let message = ''

if (userName === '1q2w3e4r') {
    message = '<h1>This is secret Admin page</h1>'
 } else if (userName === 'ssafy') {
     message = '<h1>You are from matrix</h1>'
 } else {
     message = `<h1>Hello ${userName}</h1>`
 }

 message

//  document.write(message)

 const fruits = { a: 'apple', b: 'banana' }

for (const key in fruits) {
	console.log(key) // a, b
	console.log(fruits[key]) // 1, 2
}

// const fruits = ['apple', 'banana']

// for (const index in fruits) {
// 	console.log(index) // 0, 1
// 	console.log(fruits[index]) // apple, banana
// }

let day = 2

if (day === 1){
    console.log('월요일')
} else if (day === 2){
    console.log('화요일')
} else if (day === 3){
    console.log('수요일')
} else if (day === 4){
    console.log('목요일')
} else if (day === 5){
    console.log('금요일')
} else if (day === 6){
    console.log('토요일')
} else {
    console.log('일요일')
}


switch(day){
    case 1:{
        console.log('월요일')
        break
    }
    case 2:{
        console.log('화요일')
        break
    }
    case 3:{
        console.log('수요일')
        break
    }
    case 4:{
        console.log('목요일')
        break
    }
    case 5:{
        console.log('금요일')
        break
    }
    case 6:{
        console.log('토요일')
        break
    }
    default: {
        console.log('일요일')
    }
}

let i = 0

while (i<6){
    console.log(i)
    i++
}

for (let i = 0; i < 6; i++){
    console.log(i)
}

const numbers = [0,1,2,3,4]

for (const number of numbers){
    console.log(number)
}

const fruitss = {
    'apple': 2,
    'banana': 10,
    'tomato': 10,
    'watermelon': 2,
}

for (const key in fruitss){
    console.log(key)
    console.log(fruitss[key])
}

for (let i = 0; i < 10; i++){
    if (i === 3) {
        continue
    } 
    console.log(i)
}