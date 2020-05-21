<template>
  <div>
    <div>food: <input type="text" v-model="name"></div>
    <div>quantity: <input type="text" v-model="quantity"></div>
    <div>reason: <textarea v-model="reason"></textarea></div>
    <button @click="createFood()">Submit</button>
    <div>{{ confirmation }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      name: '',
      quantity: 0,
      reason: '',
      confirmation: ''
    }
  },
  methods: {
    createFood() {
      const path = '/foods'
      const payload = {
        name: this.name,
        quantity: this.quantity,
        date: Date.now(),
        reason: this.reason
      }
      axios.post(path, payload)
        .then((res) => {
          this.displayValidation(res.data)
        })
      this.name = ''
      this.reason = ''
      this.quantity = 0
    },
    displayValidation(res) {
      console.log(res)
      this.confirmation = `${res.quantity}g of ${res.name} added on ${res.date}`
    },
  },
  created() {
    this.confirmation = ''
  }
}
</script>
