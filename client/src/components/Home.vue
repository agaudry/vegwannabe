<template>
  <div>
    <p>{{ msg }}</p>
    <h1>Do</h1>
    <div v-for="doItem in dos" :key="doItem.id">
      <p v-bind:style="[doItem.current && { fontWeight: bold }]" v-on:click="updateDo(doItem.id, doItem.name)">{{ doItem.name }}</p>
    </div>
    <h1>Don't</h1>
    <div v-for="dontItem in donts" :key="dontItem.id">
      <p>{{ dontItem.name }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      dos: '',
      donts: '',
    }
  },
  methods: {
    getDos() {
      const path = 'http://localhost:5000/doitems'
      axios.get(path).then((res) => {
        this.dos = res.data
      })
        .catch((error) => {
          console.error(error)
        })
    },
    getDonts() {
      const path = 'http://localhost:5000/dontitems'
      axios.get(path).then((res) => {
        this.donts = res.data
      })
        .catch((error) => {
          console.error(error)
        })
    },
    updateDo(itemId, itemName) {
      const path = 'http://localhost:5000/do'
      const payload = {
        id: itemId,
        name: itemName,
        datetime: Date.now()
      }
      axios.post(path, payload)
        .then(() => {
          this.getDos()
        })
    },
  },
  created() {
    this.getDos()
    this.getDonts()
  }
}
</script>
