import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default new Vuex.Store({
  state: {
    inputValue: '',
    videos: [],
    selectedVideo: null
  },
  mutations: {
    setInputValue(state) {
      console.log('MUTATION setInputValue', state)
    },
    setVideos(state) {
      console.log('MUTATION setVideos', state)
    },
    setSelectedVideo(state, video) {
      state.selectedVideo = video
      // console.log('MUTATION setSelectedVideo', state, payload)
    }
  },
  getters: {
    videoUrl(state) {
      return 'https://youtube.com/embed/' + state.selectedVideo.id.videoId
    },
    videoTitle: state => state.selectedVideo.snippet.title,
    videoDescription: state => state.selectedVideo.snippet.description,
  },
  actions: {
    fetchVideos(context, event) {
      console.log(context, event)
      context.commit('setInputValue', event.target.value)

      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: context.state.inputValue
        },
      })
      .then(res => {
        // console.log(res)
        // this.videos = res.data.items
        res.data.items.forEach(item => {
          const parser = new DOMParser()
          const doc = parser.parseFromString(item.snippet.title, 'text/html')
          item.snippet.title = doc.body.innerText
        })
        context.commit('setVideos', res.data.items)
      })
      .catch(err => console.error(err))
    }
  },
  modules: {
  }
})
