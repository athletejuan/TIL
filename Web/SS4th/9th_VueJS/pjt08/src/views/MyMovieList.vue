<template>
  <div>
    <MyListForm />
    <MyList />
  </div>
</template>

<script>
import MyList from '@/components/MyList'
import MyListForm from '@/components/MyListForm'

export default {
  name: 'MyMovieList',
  components: {
    MyList,
    MyListForm,
  }
}
</script>
