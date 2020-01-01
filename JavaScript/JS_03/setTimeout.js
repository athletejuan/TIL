// console.log('Hi')

// setTimeout(function ssafy() {
//     console.log('Bye')
// }, 3000)

// console.log('ssafy')

function printHello(){
    // console.log('4')
    console.log('Hello from baz')
}
function baz(){
    // console.log('3')
    setTimeout(printHello, 3000)
}
function bar(){
    // console.log('2')
    baz()
}
function foo(){
    // console.log('1')
    bar()
}
foo()

function func1(){
    console.log('func1')
    func2()
}
function func2(){
    setTimeout(() => console.log('func2'), 0)
    func3()
}
function func3(){
    console.log('func3')
}
func1()