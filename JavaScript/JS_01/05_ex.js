// for를 foreach로

// function handlePosts(){
//   const posts = [
//     { id: 23, title: 'Daily JS News' },
//     { id: 52, title: 'Code Refactor City' },
//     { id: 105, title: 'The Brightest Ruby' }
//   ]
//   for (let i = 0; i < posts.length; i++){
//     console.log(posts[i]) 
//     console.log(posts[i].id)
//     console.log(posts[i].title)
//   }
// }
// handlePosts()

function handlePosts(){
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
}
handlePosts()

// map
const newNumbers = [4, 9, 16]

const roots = newNumbers.map(rootNum => rootNum ** .5)
console.log(roots)

//filter
const numbers = [15,25,35,45,55,65,75,85,95]

// const filteredNumbers = numbers.filter(function(number){return number > 50})
const filteredNumbers = numbers.filter(number => number > 50)
console.log(filteredNumbers)

const users = [
  { id: 1, admin: false, name: 'eric' },
  { id: 2, admin: false, name: 'harry' },
  { id: 3, admin: true, name: 'john' },
  { id: 4, admin: false, name: 'jason' },
  { id: 5, admin: true, name: 'juan' },
]

const filteredUsers = users.filter(function(user){
  return user.admin === true
})
console.log(filteredUsers)

const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'

const api = {
  'key': 'API_KEY',
  'targetDt': '20200115'
}

const requestUrl = Object.entries(api).reduce(function(acc, el){
  return acc + `${el[0]}=${el[1]}&`
}, baseUrl)
console.log(requestUrl)

const names = ['harry','jason','tak','tak','justin']

const dupliNames = names.reduce(function(acc, name){
  if (name in acc){
    acc[name]++
  } else {
    acc[name] = 1
  }
  return acc
}, {})
console.log(dupliNames)

const people = [
  { id: 1, admin: false },
  { id: 2, admin: false },
  { id: 3, admin: true },
]

const admin = people.find(function(person){
  return person.admin
})
console.log(admin)

const accounts = [
	{ name: 'justin', balance: 1200 },
	{ name: 'harry', balance: 50000 },
	{ name: 'jason', balance: 24000 },
]

const account = accounts.find(function(account){
  return account.balance === 24000
})
console.log(account)

const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]

const status = requests.some(function(request){
  return request.status === 'pending'
})
console.log(status)

const allusers = [
  { id: 21, submmited: true },
  { id: 33, submmited: false },
  { id: 712, submmited: true},
]

const hasSubmitted = allusers.every(function(user){
  return user.submitted
})
console.log(hasSubmitted)