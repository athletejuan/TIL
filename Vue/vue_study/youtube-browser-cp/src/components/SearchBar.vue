<template>
  <div>
    <input @input="onInput" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(e){
      // input이 들어오면 inputChange 라는 이벤트와 e.target.value의 data가 상위로 emit 된다.
      this.$emit('inputChange', e.target.value);
      // console.log(e.target.value);
    }
  }
}
</script>

<style scoped>
  input {
    width: 75%;
  }
  div {
    text-align: center;
    margin: 20px;
  }
</style>