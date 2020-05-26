<template>
  <div>
    <h1>Lunch</h1>
    <p>{{ menus.join(',') }}</p>
    <!-- <li v-for="menu in menus" :key="menu">{{ menu }}</li> -->
    <button @click="pick">랜덤선택</button>

    <p>{{ choice }}</p>
  </div>
</template>

<script>
// const _ = require('lodash')
import _ from 'lodash'
export default {
  data: function(){
    return {
      menus: ['짜장', '짬뽕', '김밥', '라면'],
      choice: '',
    }
  },
  methods: {
    pick(){
      this.choice = _.sample(this.menus)
    }
  }
}
</script>

<style>

</style>