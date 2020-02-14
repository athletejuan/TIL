const axios = require('axios')
// console.log(axios)

url = 'https://jsonplaceholder.typicode.com/todos/1'

const res = axios.get(url)
console.log(res)

res
  .then((res)=>{
    // console.log(res)
    console.log(res.data.title)
  })
  .catch((err)=>{
    // console.log(err)
  })