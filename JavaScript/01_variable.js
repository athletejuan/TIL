// 01.1 변수(variable)

// let(변수)
let x = 1
// let x = 2 Bad
// x = 3 Good
// x

// 블록 유효 범위(block scope)
// if, for문 그리고 함수에서의 중괄호({})내부를 가리킨다.

if (x === 1) {
    let x = 2
    console.log(x)
}
console.log(x)


// const(상수)
// myFav를 상수로 정의하고 그 값을 7로 정함
const myFav = 7

// 7 출력
console.log('my favorite number is: ' + myFav)

// node에서 진행하는 경우 에러 발생 코드 작성 후 반드시 주석 처리
// 재할당을 하려고하면 에러가 발생함(assignment)
// myFav = 20

// 블록 범위의 특성을 아는게 중요
if (myFav === 7){
    // 블록 범위로 지정된 myFav 라는 변수를 만드므로 괜찮습니다.
    // 즉, 전역이 아닌 범위이므로 이름 공간에서 충돌이 나지 않습니다.
    // (let으로 const 변수가 아닌 블록 범위를 선언하는 것과 똑같이 동작합니다.)
    const myFav = 20 // const는 재선언이 불가능하기 때문에 let으로 설정

    // myFav는 이제 20
    console.log('my favorite number is ' + myFav)
}

console.log(myFav) // 7


// var(변수)
function varTest() {
    var x = 1
    if (true) {
        var x = 2 // 상위 블록과 같은 변수
        console.log(x) // 2
    }
    console.log(x) // 2
}

varTest()

// let
function letTest() {
    let x = 1
    if (true) {
        let x = 2 // 상위 블록과 같은 변수
        console.log(x) // 2
    }
    console.log(x) // 1
}

letTest()

var a = 1
let b = 2

if (a === 1) {
    var a = 11 // 전역 변수
    let b = 22 // if 블록 변수

    console.log(a) // 11
    console.log(b) // 22
}

console.log(a) // 11
console.log(b) // 2

// var: 할당 및 선언 자유, 함수 스코프
// let: 할당 자유, 선언은 한번만, 블록 스코프
// const: 할당 및 선언 한번만, 블록 스코프


// 01.2 식별자(Identifier)
// camelCase - 객체, 변수, 함수
// 숫자, 문자, 불린
let dog
let variableName

// 배열 - 배열은 복수형 이름을 사용
const dogs = []

// 정규표현식 - 정규표현식은 'r'로 시작
const rDesc = /.*/

// 함수
function getPropertyName() {}

// 이벤트 핸들러 - 이벤트 핸들러는 'on'으로 시작
const onClick = {}
const onKeyDown = {}

// 불린 반환 함수 - 반환 값이 불린인 함수는 'is'로 시작
let isAvailable = false

// PascalCase - 클래스, 생성자
class User {
    constructor(options){
        this.name = options.name
    }
}

const good = new User({
    name: 'ryu'
})

// SNAKE_CASE - 상수
// 실제 동작하는 코드는 아님
// export const API_KEY = 'SOMEKEY'
// export const MAPPING = {
//     key = 'value'
// }


// 01.3 Hoisting
// 된다!
console.log(a) // undifined - 선언(할당아님)만 최상단으로 끌어올려진다.
var a = 10
console.log(a) // 10

// 아래와 같은 과정을 거친다.
var a // 1. 선언이 최상단으로
console.log(a) // 2. 그래서 에러가 나지않고 undifined
a = 10 // 3. 할당은 그 뒤에
console.log(a)

// let 은 안된다
// console.log(b)
// let b = 10
// console.log(b)

// 마찬가지로 아래와 같은 과정을 거친다.
// let b
// console.log(b)
// b = 10
// console.log(b)
// 왜 안될까?

// var(함수 스코프) / let(블록 스코프)
// var 할당 과정
// 1. 선언 - 초기화 (동시 진행)
// 2. 할당

// let, const 할당 과정
// 1. 선언
// 2. TDZ(Temporal Dead Zone, 임시적 사각지대)
// 3. 초기회
// 4. 할당
// (결국 초기화 이전에 변수에 접근하게 되면서 TDZ에 의해 에러발생)

var a // 선언 + 초기화로 인해 undefined로 메모리에 할당
console.log(a)
a = 10
console.log(a)

// let b // 선언
// console.log(b)
// b = 10 // 초기화되지 않았는데 할당하려 함
// console.log(b)

// 주의사항은 위 코드만 단독적으로 사용했을 때는 let 도 undefined 가 출력된다
// JS 가 내부적으로 이해한 코드이기 때문에 직접 입력하는것과는 다르다.

if (w !== 1){
    console.log(z) // undifined
    var z = 3
    if (z === 3){
        var w = 1
    }
    console.log(z) // 3
}
if (w === 1) {
    console.log(z) // 3 (var는 function scope이기 때문에 함수가 아니면 전역 취급)
}

// JS 가 해석한 코드
var w
var z

if (w !== 1){
    console.log(z) // undifined
    var z = 3
    if (z === 3){
        var w = 1
    }
    console.log(z) // 3
}
if (w === 1) {
    console.log(z) // 3 (var는 function scope이기 때문에 함수가 아니면 전역 취급)
}