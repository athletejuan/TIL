<template>
  <div>
    <h1>Lunch</h1>
    <p>{{ menus.join(',') }}</p>
    <button @click="pick">랜덤 선택</button>
    <p>{{ choice }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  data: function(){
    return {
      menus: ['짜장', '짬뽕', '김밥', '고등어회', '닭볶음탕'],
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