// "Hello!!!"
function greet(){
    return "Hello!!!"
}
// greet()
// Promise {<resolved>: "Hello!!!"}
async function greet(){
    return "Hello!!!"
}
// console.log(greet())
// Promise resolved with: Hello!!!
greet()
.then((res) => {
    console.log('Promise resolved with: ', res)
})

// Promise rejected with: X and Y must be numbers!
//
function add(x,y){
    return new Promise((resolve, reject) => {
        if (typeof x === 'number' || typeof y !== 'number'){
            reject('X and Y must be numbers!')
        }
        resolve (x + y)
    })
}

add('e','r') // add(4,5)
.then((res) => {
    console.log('Promise resolved with: ', res)
})
.catch((err) => {
    console.log('Promise rejected with: ', err)
})

console.log(add())