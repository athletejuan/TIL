const numbersAddEach = numbers => {
    let sum = 0
    for (const number of numbers) {
        sum += number
    }
    return sum
}
console.log(numbersAddEach([1,2,3,4,5]))

const numbersSubEach = numbers => {
    let sum = 0
    for (const number of numbers) {
        sum -= number
    }
    return sum
}
console.log(numbersSubEach([1,2,3,4,5]))

const numbersMulEach = numbers => {
    let sum = 1
    for (const number of numbers) {
        sum *= number
    }
    return sum
}
console.log(numbersMulEach([1,2,3,4,5]))


// functionalization(함수화)

const numbersEach = (numbers, callback) => {
    let acc
    for (const number of numbers) {
        acc = callback(number, acc) // [??? 한다] === callback
    }
    return acc
}

const NUMBERS = [1,2,3,4,5]

const addEach = (number, acc = 0) => {
    return acc + number
}
console.log(numbersEach(NUMBERS, addEach))

const subEach = (number, acc = 0) => {
    return acc - number
}
console.log(numbersEach(NUMBERS, subEach))

const mulEach = (number, acc = 1) => {
    return acc * number
}
console.log(numbersEach(NUMBERS, mulEach))


// anonymous functionalization(익명 함수화)

console.log(numbersEach(NUMBERS, (number, acc = 0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc = 1) => acc * number))