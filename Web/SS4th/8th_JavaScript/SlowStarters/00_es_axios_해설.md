## 문제 I - ES

### 1. 조건 & 반복

> 주어진 배열에 속한 숫자의 0/홀/짝 여부를 판별하는 코드를 작성하시오.

```javascript
const numbers = [0, 1, 2, 3, 4, 5, 6]
```

![problem_01](00_es_axios_해설.assets/problem_01.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    const numbers = [0, 1, 2, 3, 4, 5, 6]

    for (let number of numbers) {
      if (number === 0) {
        console.log(`${number}은 0입니다.`)
      } else if (number % 2) {
        console.log(`${number}은(는) 홀수입니다.`)
      } else {
        console.log(`${number}은(는) 짝수입니다.`)
      }
    }
  </script>
</body>
</html>

```





### 2. Array Helper Method - `forEach`

> 아래 todos 배열에서 `content`에 해당하는 내용을 콘솔에 출력하시오.

```javascript
const todos = [
  { "id": 1, "title": "제목1", "content": "내용1" },
  { "id": 2, "title": "제목2", "content": "내용2" },
  { "id": 3, "title": "제목3", "content": "내용3" },
]
```

![problem_02](00_es_axios_해설.assets/problem_02.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    const todos = [
      { "id": 1, "title": "제목1", "content": "내용1" },
      { "id": 2, "title": "제목2", "content": "내용2" },
      { "id": 3, "title": "제목3", "content": "내용3" },
    ]

    todos.forEach(function (todo) {
      console.log(todo.content)
    })
  </script>
</body>
</html>
```



## 문제 II - Axios

> Axios를 활용해 https://jsonplaceholder.typicode.com/todos/ 보낸 요청의 응답 결과 중 title 정보를 활용해 아래 그림과 같은 결과를 만드시오.

![problem_03](00_es_axios_해설.assets/problem_03.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <ul id="myUl"></ul>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    axios.get('https://jsonplaceholder.typicode.com/todos/')
      .then(function (response) {
        const todos = response.data
        const myUl = document.querySelector('#myUl')

        todos.forEach(function (todo) {
          const myLi = document.createElement('li')
          myLi.innerText = todo.title
          myUl.append(myLi)
        })
      })
  </script>
</body>
</html>
```

