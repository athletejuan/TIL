<template>
  <div class="home">
    <TeamProfile :newMessage="newMessage" :members="members" @getNewMessage="getNewMessage">
    </TeamProfile>
  </div>
</template>

<script>
// @ is an alias to /src
import TeamProfile from '@/components/TeamProfile.vue'

export default {
  name: 'Home',
  props: {
    // newMessage: Object,
    // members: Array,
  },
  components: {
    TeamProfile
  },
}
</script>

<style scoped>
  .home {
    text-align: center;
  }
</style>