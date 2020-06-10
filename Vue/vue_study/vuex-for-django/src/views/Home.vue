<template>
  <div>
    <h1>Article List</h1>
    <li v-for="article in articles" :key="article.id">{{ article.title }} - {{ article.user.username }}</li>
  </div>
</template>
<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Home',
  data() {
    return {
      articles: null,
    }
  },
  methods: {
    getArticles() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }

      axios.get(`${BACK_URL}/articles/`, requestHeaders)
        .then(res => {
          this.articles = res.data
        })
        .catch(err => {
          console.log(err.response)
        })
    }
  },
  mounted() {
    this.getArticles()
  }
}
</script>