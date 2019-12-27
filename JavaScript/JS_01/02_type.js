// const a = 13
// const b = -5
// const c = 3.14 // float - 숫자표현
// const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
// const e = Infinity
// const f = -Infinity
// const g = NaN // Not a Number

// console.log(a,b,c,d,e,f,g)

const happy = 'Will you join us?'
const hacking = 'Happy' + 'Hacking' + '!'
console.log(happy, hacking)

const a = 1
const b = '1'

console.log(a == b) // true 
console.log(a != b) // false

console.log(a == Number(b)) // true - Number를 통해 숫자로 형변환


// 자동 형변환 예시
console.log(8 * null)  // 0, null은 0
console.log('5' - 1)  // 4
console.log('5' + 1)  // 51
console.log('five' * 2)  // NaN

const result = Math.PI > 3 ? 'Yep' : 'Nope'
console.log(result) // Nope