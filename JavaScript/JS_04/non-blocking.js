const axios = require('axios')
url = 'https://www.naver.com'

// Promise 방식
// axios.get(url)
//     .then(response => {
//         console.log(response.data)
//     })

// 3. Async Await 방식
// async function sendRequest(url){
//     response = await axios.get(url)
//     console.log(response.data)
// }

// sendRequest(url)

function getDataAsync(url){
    return new Promise(resolve => {
        setTimeout(function(){
            console.log('요청을 보냈습니다.')
            const data = {'data': 'blahblah'}
            resolve(data) // 이행
        }, 1000)
    })
}
async function read() {
    var response = await getDataAsync()
    console.log(response)
}
read()