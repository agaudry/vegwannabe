<template>
  <div class="p-4 h-screen font-sans">
    <NavBar v-bind:displayLogin="true"/>
    <ul>
      <li v-for="food in foods" :key="food.id"> {{ food.name }} </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import NavBar from './NavBar.vue'

export default {
  name: 'Foods',
  components: {
    NavBar,
  },
  data() {
    return {
      foods: {},
    }
  },
  methods: {
    getFoods() {
      const path = '/foods'
      const cookie = document.cookie
      const headers = { headers: { 'Authorization': `JWT ${cookie.split('=')[1]}` } }
      axios.get(path, headers)
        .then((res) => {
          this.foods = res.data
        })
    },
  },
  created() {
    this.getFoods()
  }
}
</script>
