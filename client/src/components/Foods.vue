<template>
  <div class="p-4 h-screen font-sans">
    <NavBar />
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
      axios.get(path)
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
