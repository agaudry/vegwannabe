<template>
  <div>
    <p>{{ msg }}</p>
    <p>{{ title }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      msg: '',
      title: '',
    }
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/'
      axios.get(path).then((res) => {
        this.msg = res.data
      })
        .catch((error) => {
          console.error(error)
        })
    },
    getDos() {
      const path = 'http://localhost:5000/do'
      axios.get(path).then((res) => {
        this.title = res.data
      })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created() {
    this.getMessage()
    this.getDos()
  }
}
</script>
