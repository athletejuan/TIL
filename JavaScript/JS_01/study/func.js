// def hello():
//     print("hi")

function hello(name){
    console.log(`${name} hi`)
}

hello('change')

const greeting = function(name){
    console.log(`${name} hi`)
}

greeting('change')

// const hi = name => {}
const hi = (name) => {
    console.log(`${name} hi`)
}
hi('change')

// 인자가 하나면 () 생략가능
const hi2 = name => {
    return`${name} hi`
}
hi2('change')

const hi3 = name => `${name} hi`
hi3('change')