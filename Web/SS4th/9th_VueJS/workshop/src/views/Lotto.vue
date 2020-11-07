<template>
  <div>
    <h2>로또</h2>
    <button @click="lucky">sampleSize</button>
    <button @click="getRandom">random</button>
    <p>{{ luckyNums }}</p>
    <p>{{ randomNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Lotto',
  data: function () {
    return {
      luckyNums: '',
      randomNums: '',
    }
  },
  methods: {
    lucky() {
      const sampleNums = _.sampleSize(_.range(1, 46), 6)
      this.luckyNums = sampleNums
    },
    getRandom: function() {
      this.randomNums = []
      while (this.randomNums.length < 6) {
        const randomNum = _.random(1,45)
        if (!this.randomNums.includes(randomNum)) {
          this.randomNums.push(randomNum)
        }
      }
    }
  }
}
</script>

<style>

</style>