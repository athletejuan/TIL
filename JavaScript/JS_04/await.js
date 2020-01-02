const axios = require('axios')

// 1. 
function getPlanets(){
    return axios.get('https://swapi.co/api/planets/')
}

// getPlanets()
// .then((res) => {
//     console.log(res.data)
// })

// 2. .then이 필요 x
// await 키워드를 빼버리면 서버로부터 데이터가 오기전에 console.log가 실행되어 undifined

async function getPlanets(){
    const res = await axios.get('https://swapi.co/api/planets/sdfsdf')
    console.log(res.data)
}
getPlanets()

// 1. 첫 번째 에러 처리 방법 - catch
// getPlanets()
// .catch((err) => {
//     console.log("Error Catch!")
//     console.log(err)
// })

// 2. 두 번째 에러 처리 방법 - try & catch
async function getPlanets(){
    try{
        const res = await axios.get('https://swapi.co/api/planets/sdfsdf')
        console.log(res.data)
    } catch (err) {
        console.log("Error Catch!!", err)
    }
}
getPlanets()