<template>
  <div id="app">
    <Header></Header>
    <router-view :newMessage="newMessage" :members="members" @getNewMessage="getNewMessage" />
    <Footer></Footer>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
  data: function() {
    return {
      message: '',
      member: {},
      members: [
        {
          name: 'juan',
          age: 37,
          img: 'https://avatars3.githubusercontent.com/u/48536433?s=460&u=0e6bcff3e88d19fefccf10a8e2350b6995bfd70c&v=4',
          messages: ['안녕하세요']
        },
        {
          name: 'eric',
          age: 29,
          img: 'https://avatars1.githubusercontent.com/u/26497426?s=460&u=f0168d9c8227659e7bdcc3e118b3935291459438&v=4',
          messages: ['안녕하세요']
        },
        {
          name: 'tony',
          age: 29,
          img: 'https://avatars1.githubusercontent.com/u/44995141?s=460&u=2d5b28e1f068dbf1bf81d015ae68bf4e0055011c&v=4',
          messages: ['안녕하세요']
        },
        {
          name: 'ciao',
          age: 28,
          img: 'https://avatars3.githubusercontent.com/u/45933654?s=460&u=f75e012ced3de15a8484b2ad7d22a0ac80528a4b&v=4',
          messages: ['안녕하세요']
        },
      ]
    }
  },
  methods: {
    getNewMessage(newMessage, newMember) {
      let newMembers = this.members.map( member => {
        if (member.name === newMember.memberName) {
          let newMessages = [...member.messages, newMessage]
          let updatedMember = {...member, messages: newMessages}
          return updatedMember
        } else {
          return member
        }
      })
      this.members = newMembers
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
