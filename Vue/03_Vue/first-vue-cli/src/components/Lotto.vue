<template>
  <div>
    <h1>Lotto</h1>
    <button @click="getNums">숫자생성</button>
    <p>{{ selected }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  data: function(){
    return {
      numbers: _.range(1,46),
      selected: '',
    }
  },
  methods: {
    getNums: function(){
      this.selected = _.sampleSize(this.numbers, 6)
    }
  }
}
</script>

<style>

</style>