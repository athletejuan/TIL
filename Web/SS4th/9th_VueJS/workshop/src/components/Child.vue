<template>
  <div id="child">
    <h2>Child</h2>
    <input v-model="childData" @input="onInput" type="text">
    <!-- <input @input="onInput" type="text"> -->
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  data: function () {
    return {
      childData: '',
    }
  },
  props: {
    appData: {
      type: String,
    },
    parentData: {
      type: String,
    }
  },
  methods: {
    onInput: function() {
      this.$emit('child-input', this.childData)
      // this.$emit('child-input', event.target.value)
    }
  }
}
</script>

<style>
  #child {
    margin: 1rem;
    border: 1px solid blue;
  }
</style>