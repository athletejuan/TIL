<template>
  <div>
    <h1>Lunch</h1>
    <p>{{ menus }}</p>
    <button @click="pick">랜덤선택</button>
    <p>{{ choice }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  data: function() {
    return {
      menus: ['짜장', '짬뽕', '김밥', '라면'],
      choice: '',
    }
  },
  methods: {
    pick: function(){
      this.choice = _.sample(this.menus)
    }
  }
}
</script>

<style>

</style>