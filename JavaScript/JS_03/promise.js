const MyInfo = {
    name: 'juan',
    phoneNumber: '010-1234-5678',
    greeting: function() {
        console.log(this.name + 'hi')
    }
}
console.log(MyInfo)

let name = 'justin'
let greeting = function() {
    console.log(this.name + ' hi')
}
const YourInfo = {
    name,
    greeting
}
console.log(YourInfo)

const Person = function(name){
    this.name = name
    this.greeting = function(){
        console.log(this.name + ' hi')
    }
}
const juan = new Person('juan')

console.log(juan)

// 1. 동기적 처리방식
// function getData(){
//     const data = {'data': 'blahblah'}
//     return data
// }

// function printData1(){
//     let response1 = getData()
//     console.log(response1)
// }
// printData1()

// getData 내에 let을 사전에 정의하는 이유는
// setTimeout에서 data에 넣지만 undefined가 return 되도록 구성하기 위해서

// 2. 비동기적 처리방식(문제)
// function getData(){
//     let data
//     setTimeout(function(){
//         console.log('요청을 보냈습니다.')
//         data = {'data': 'somesome'}
//     }, 1000)
//     return data
// }

// function printData2(){
//     let response2 = getData()
//     console.log(response2) // undifined
// }
// printData2()

// 3. 비동기적 처리방식(해결)
// function getDataCallBack(callback){ // 2nd. callback으로 넘어옴, 즉 callback = 익명함수
//     setTimeout(function(){
//         console.log('요청을 보냈습니다.')
//         const data = {'data': 'exciting'}
//         callback(data) // 3rd. 다 끝나고 저 함수를 호출
//     }, 1000)
// }
// // 1st. 출력하는 작업을 하는 익명함수를 인자로 넘김
// getDataCallBack(function(response){
//     console.log(response)
// })


// 1.
function getDataPromise(){
    // Promise 오브젝트를 반환!
    return new Promise(resolve => {
        setTimeout(function(){
            console.log('요청을 보냈어요.')
            const data = {'data': 'wowwow'}
            resolve(data) // 이행
        }, 100)
    })
}

function myPromise(){
    return new Promise((resolve, reject) => {
        if (url == 'http'){
            resolve('성공') // 이행 -> then으로 호출
        } else {
            reject('실패') // 거절 -> catch로 호출
        }
    })
}

var promise1 = myPromise()
console.log(promise1) // promise 객체
var promise2 = myPromise()
console.log(promise2)
promise1.then(msg => console.log(msg))
promise2.catch(e => console.log(e))

const myPromise2 = url => new Promise((resolve, reject) => {
    if (url == 'http') {
        resolve('성공') // 이행 -> then으로 호출
    } else {
        reject('실패') // 거절 -> catch로 호출
    }
})

getDataPromise('http')
.then(response => {
    console.log(response)
    return response.data // Promise의 return값을 .then으로 이어받아 처리가능
})
.then(data => {
    console.log(data)
})
// var response3 = getDataPromise()
// console.log(response3) // Promise {<pending>}

const axios = require('axios');

axios.get('https://jsonplaceholder.typicode.com/posts/1')
    .then(response => {
      console.log(response)
      return response.data.userId
    })
    .then(userId => 
      axios.get(`https://jsonplaceholder.typicode.com/users/${userId}`)
    )
    .then(response => {
      console.log(response)
      console.log(response.data.username)
    })