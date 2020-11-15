<template>
  <div class="p-4 h-screen font-sans">
    <NavBar v-bind:displayLogin="true"/>
    <div class="px-4 py-20 text-light">
      <span class="font-bold text-lg">I ate</span>
      <div class="grid grid-cols-12 gap-4 mt-2">
        <div class="col-span-9 border-b border-pop">
          <input class="appearance-none bg-pop bg-opacity-25 text-pop text-md focus:outline-none w-full" placeholder="Beef" type="text" v-model="name">
        </div>
        <div class="col-span-2 border-b border-pop">
          <input class="appearance-none bg-pop bg-opacity-25 text-pop text-md focus:outline-none w-full" placeholder="100" type="text" v-model="quantity">
        </div>
        <div class="col-span-1 font-bold text-lg">g</div>
      </div>
      <div class="mt-4 mb-2">
        <span class="font-bold text-lg">Because</span>
        <textarea class="h-8 mt-2 p-1 border border-pop rounded appearance-none bg-transparent text-pop text-sm focus:outline-none w-full" placeholder="My mom cooked it" v-model="reason"></textarea>
      </div>
      <button @click="createFood()" class="focus:outline-none mt-4 rounded bg-light bg-opacity-50 border-light border border-opacity-100 px-2 py-1 text-dark font-bold">Submit</button>
      <div>{{ confirmation }}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import NavBar from './NavBar.vue'

export default {
  name: 'Home',
  components: {
    NavBar,
  },
  data() {
    return {
      name: '',
      quantity: null,
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
      this.confirmation = `${res.quantity}g of ${res.name} added on ${res.date}`
    },
  },
  created() {
    this.confirmation = ''
  }
}
</script>
