<template>
  <div class="member-detail">
    <div class="member-detail--left">
      <div class="member-image" :style="{ background: 'url(' + memberImage + ')' }"></div>
      <h1>{{memberName}}</h1>
    </div>
    <div class="member-detail--right">
      <form @submit="submitMessage($event, {memberName, memberImage, memberMessages})">
        <input type="text" v-model="userInput">
        <input type="submit" value="작성">
      </form>
      <div class="member-detail--messages" v-for="(message, idx) in memberMessages" :key="idx">
        {{message}}
      </div>
    </div>
    <MemberProfile></MemberProfile>
  </div>
</template>
<script>
import MemberProfile from '../components/MemberProfile'

export default {
  name: "MemberDetail",
  props: {
    // newMessage: Object,
  },
  components: {
    MemberProfile,
  },
  created() {
    this.memberName = this.$route.query.memberName
  },
  data: function() {
    return {
      memberName: '',
      memberImage: this.$route.query.memberImage || '',
      memberMessages: this.$route.query.memberMessages || [],
      userInput: '',
      isRendered: false,
    }
  },
  methods: {
    submitMessage(event, member) {
      event.preventDefault()
      this.memberMessages.push(this.userInput)
      // this.$emit('getNewMessage', this.userInput, member)
      this.$store.commit('updateMembers', {newMessage: this.userInput, member})
    }
  }
}
</script>