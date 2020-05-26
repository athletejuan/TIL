<template>
  <div>
    <h1>Lunch</h1>
    <li v-for="menu in menus" v-bind:key="menu">{{ menu }}</li>
    <button @click="pick">선택</button>
    <p>{{ choice }}</p>
  </div>
</template>

<script>
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