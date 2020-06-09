<template>
  <div>
    <h1>create</h1>
    title : <input type="text" v-model="title">
    <br>
    content : <input type="text" v-model="content">
    <br>
    <button @click="createArticle">create</button>
  </div>
</template>
<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const requestForm = new FormData()
      requestForm.append('title', this.title)
      requestForm.append('content', this.content)

      axios.post(`${BACK_URL}/articles/create/`, requestForm, requestHeaders)
       .then(() => {
         this.$router.push('/articles/')
       })
       .catch(err => {
         console.log(err.response)
       })
    }
  }
}
</script>