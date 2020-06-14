<template>
  <div class="team-profile">
    <div class="team-profile-baseline">
      <h1 class="team-profile--title">HPHK.</h1>
      <p class="team-profile--subtitle">각 멤버에게 방명록을 남겨주세요!</p>
      <MemberProfile v-for="(member, idx) in members" :key="idx" :member="member"></MemberProfile>
    </div>
  </div>
</template>
<script>
import MemberProfile from '@/components/MemberProfile'
export default {
  name: 'TeamProfile',
  props: {
    // members: Array,
  },
  components: {
    MemberProfile
  },
  computed: {
    getMembers() {
      return this.$store.getters.getMembers
    }
  }
}
</script>