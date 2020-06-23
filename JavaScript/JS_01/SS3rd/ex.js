// 조건문

// let day = 2

for (let i = 1; i < 8; i++) {
  if (i == 1) {
    console.log('월요일')
  } else if (i == 2) {
    console.log('화요일')
  } else if (i == 3) {
    console.log('수요일')
  } else if (i == 4) {
    console.log('목요일')
  } else if (i == 5) {
    console.log('금요일')
  } else if (i == 6) {
    console.log('토요일')
  } else {
    console.log('일요일')
  }
}

for (let day = 1; day < 8; day++){
  switch(day){
    case 1: {
      console.log('월요일')
      break
    }
    case 2: {
      console.log('화요일')
      break
    }
    case 3: {
      console.log('수요일')
      break
    }
    case 4: {
      console.log('목요일')
      break
    }
    case 5: {
      console.log('금요일')
      break
    }
    case 6: {
      console.log('토요일')
      break
    }
    default: {
      console.log('일요일')
    }
  }
}

// 반복문

let num = 0

while (num < 6) {
  console.log(num)
  num++
}

for (let num = 0; num < 6; num++) {
  console.log(num)
}

const numbers = [0,1,2,3,4]

for (number of numbers) {
  console.log(number)
}

const fruits = {
  'apple': 2,
  'banana': 10,
  'tomato': 10,
  'watermelon': 2,
}

for (fruit in fruits) {
  console.log(fruit, fruits[fruit])
}

for (let i = 0; i < 10; i++) {
  if (i === 3) {
    continue
  } else {
    console.log(i)
  }
}