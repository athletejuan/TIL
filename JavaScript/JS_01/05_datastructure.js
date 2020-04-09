// Array

const numbers = [1,2,3,4]

numbers[0]
console.log(numbers[-1])
console.log(numbers.length)

numbers.reverse()
console.log(numbers)
numbers.reverse()
console.log(numbers)

numbers.push('a')
console.log(numbers)
console.log(numbers.pop()) // 'a', 가장 마지막 요소
console.log(numbers)

numbers.unshift('a') // 5, 새로운 배열의 길이
console.log(numbers)
console.log(numbers.shift()) // 'a', 가장 처음 요소
console.log(numbers)

console.log(numbers.includes(1)) // true
console.log(numbers.includes(0)) // false

numbers.push('a','a')
console.log(numbers)
console.log(numbers.indexOf('a'))
console.log(numbers.indexOf('b'))

console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join('-'))


// Object

const me = {
    name: '홍길동', // key가 한 단어일 때
    'phone number': '01012345678', // key가 여러 단어일 때
    appleProducts: {
        ipad: '2018pro',
        iphone: '11pro',
        macbook: '2019pro',
    },
}

console.log(me.name)
console.log(me['name'])
console.log(me['phone number'])
console.log(me.appleProducts)
console.log(me.appleProducts.ipad)

// Object to array
const fruits_obj = {a: 'apple', b: 'banana'}
console.log(Object.keys(fruits_obj))
console.log(Object.values(fruits_obj))
console.log(Object.entries(fruits_obj))

let books = ['Learning JS', 'Eloquent JS']

let comics = {
    DC: ['Aquaman', 'SHAZAM'],
    Marvel: ['Captain Marvel', 'Avengers'],
}

let magazines = null

const bookShop = {
    books,
    comics,
    magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// JSON -> Object
// key-value의 형태로 JS Object와 유사한 모습으로 데이터를 표현하는 표기법
// 모습만 비슷할 뿐, 실제로는 문자열 타입(String type)이다.
// Object처럼 사용하기 위해서는 parsing(구문 분석) 작업이 필요하다.

const jsonData = JSON.stringify({
    coffee: 'Americano',
    iceCream: 'Cookie and cream',
})

console.log(jsonData)
console.log(typeof jsonData)

// Object -> JSON

const parsedData = JSON.parse(jsonData)

console.log(parsedData)
console.log(typeof parsedData)

// Array Helper Method

// console.log(arr.forEach(callback(element, index, array)))

const colors = ['red','blue','green']

colors.forEach(function(color){
    console.log(color)
})

// refactoring
colors.forEach(color => console.log(color))

const result = colors.forEach(color => console.log(color))
console.log(result) // undifined

const images = [
    {height: 10, width: 30},
    {height: 20, width: 90},
    {height: 54, width: 32}
]

const areas = []

// answer
images.forEach(function(image){
    areas.push(image.height * image.width)
})

console.log(areas)

function handlePosts() {
    const posts = [
      { id: 23, title: 'Daily JS News' },
      { id: 52, title: 'Code Refactor City' },
      { id: 105, title: 'The Brightest Ruby' }
    ]

    posts.forEach(function(post){
        console.log(post)
        console.log(post.id)
        console.log(post.title)
    })
    // for (let i = 0; i < posts.length; i++){
    //     console.log(posts[i]) 
    //     console.log(posts[i].id)
    //     console.log(posts[i].title)
    // }
}

handlePosts()

// map

const nums = [1,2,3]

const doubleNumbers = nums.map(function(num){
    return num * 2
})
console.log(doubleNumbers) // [2,4,6]

const newNums = [4,9,16]

// answer

const roots = newNums.map(Math.sqrt)
console.log(roots)

const pics = [
    { height: '34px', width: '39px'},
    { height: '54px', width: '19px'},
    { height: '83px', width: '75px'},
]

// heights = []

// pics.forEach(function(pic){
//     heights.push(pic['height'])
// })

// console.log(heights)

const heights = pics.map(function(pic){
    return pic.height
})
console.log(heights)

const trips = [
    {distance: 34, time: 10},
    {distance: 90, time: 50},
    {distance: 59, time: 25},
]

const speeds = trips.map(function(trip){
    return (trip.distance / trip.time)
})

console.log(speeds)

const brands = ['Marvel', 'DC']
const movies = ['IronMan','Batman']

const comicheros = brands.map((x,y) => {return {name:x, hero:movies[y]}})
console.log(comicheros)

const products = [
    {name: 'cucumber', type: 'vegetable'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'apple', type: 'fruit'},
]

const fruits = products.filter(function(product){
    return product.type === 'fruit'
})

// refactoring
// const fruits = products.filter(product => product.type === 'fruit')
console.log(fruits)

const numberss = [15, 25, 35, 45, 55, 65, 75, 85, 95]

// answer
const filteredNumbers = numberss.filter(function(number){
    return number > 50
})
console.log(filteredNumbers)

const users = [
    { id: 1, admin: false, name: 'eric'},
    { id: 2, admin: false, name: 'harry'},
    { id: 3, admin: true, name: 'john'},
    { id: 4, admin: false, name: 'jason'},
    { id: 5, admin: true, name: 'juan'},
]

const filtereduser = users.filter(function(user){
    return user.admin === true
})

console.log(filtereduser)