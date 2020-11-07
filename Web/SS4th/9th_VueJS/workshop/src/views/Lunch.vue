<template>
  <div>
    <h2>점심메뉴</h2>
    <button @click="pickOne">Pick One</button>
    <p>{{ choice }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Lunch',
  data: function () {
    return {
      lunch: ['국밥', '짜장면', '햄버거', '떡볶이'],
      choice: '',
    }
  },
  methods: {
    pickOne: function() {
      const randomIdx = _.random(0, this.lunch.length - 1)
      this.choice = this.lunch[randomIdx]
    }
  }
}
</script>

<style>

</style>