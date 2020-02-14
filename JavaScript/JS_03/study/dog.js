const axios = require('axios')

url = 'https://dog.ceo/api/breeds/image/random'
axios.get(url)
  .then(response => console.log(response.data.message))