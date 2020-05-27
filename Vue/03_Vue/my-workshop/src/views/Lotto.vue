<template>
  <div>
    <h1>Lotto</h1>
    <button @click="pick">로또번호생성</button>
    <p>행운의 번호: {{ selected }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  data: function(){
    return {
      numbers: _.range(1,46),
      selected: [],
    }
  },
  methods: {
    // getNums: function(){
    //   this.selected = _.sampleSize(this.numbers, 6)
    // },
    pick: function() {
        while (this.selected.length < 6) {
            const randpick =_.random(1, 45)
            // console.log(randpick)
            if (!this.selected.includes(randpick)) {
                this.selected.push(randpick)
            }
        }
        this.selected.sort()
    }
  }
}
</script>

<style>

</style>