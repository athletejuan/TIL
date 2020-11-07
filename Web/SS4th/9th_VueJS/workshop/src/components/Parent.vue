<template>
  <div id="parent">
    <h2>Parent</h2>
    <input v-model="parentData" @input="onInput" type="text">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child :appData="appData" :parentData="parentData" @child-input="onChildInput" />
  </div>
</template>
<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    onInput: function() {
      this.$emit('parent-input', this.parentData)
    },
    onChildInput: function(text) {
      this.childData = text
      this.$emit('child-input', text)
    },
  },
  components: {
    Child,
  },
  props: {
    appData: {
      type: String,
    },
  },
}
</script>

<style>
#parent {
  margin: 1rem;
  border: 1px solid red;
}
</style>