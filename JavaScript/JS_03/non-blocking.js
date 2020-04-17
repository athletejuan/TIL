const axios = require('axios')
url = 'https://www.naver.com'

// 1. 파이썬 방식 -> undifined
let response = axios.get(url)
console.log(response.data)

// 2. 자바스크립트 방식
axios.get(url)
.then(response => {
  console.log(response.data)
})