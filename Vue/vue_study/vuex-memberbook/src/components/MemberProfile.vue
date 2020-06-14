<template>
  <div class="member-profile">
    <div class="member-image" :class="['member-image-' + member.name]"
            :style="{ background: 'url(' + member.img + ')' }"
            v-on:click="$router.push({ 
                                        path: `/member/${member.name}`, 
                                        query: {
                                            memberName : member.name,
                                            memberImage: member.img,
                                            memberMessages: member.messages
                                            }})">
      <p class="member-messages">{{ member.messages.length }}</p>
      <p class="member-name">{{ member.name }}</p>
    </div>
  </div>
</template>
<script>
export default {
  
}
</script>