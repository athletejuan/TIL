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

