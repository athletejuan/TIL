const fco = function(){
    return n => n + 1
}
console.log(fco)

const num_101 = fco()(100)
console.log(num_101)

const fco1 = function(n){
    return n + 1
}
console.log(fco1(100))