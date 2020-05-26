<template>
  <div>
    <h1>Lotto</h1>
    <button @click="getNums">로또번호생성</button>
    <p>{{ lucky }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  data: function(){
    return {
      numbers: _.range(1,46),
      lucky: '',
    }
  },
  methods: {
    getNums: function(){
      this.lucky = _.sampleSize(this.numbers, 6)
    }
  }
}
</script>

<style>

</style>