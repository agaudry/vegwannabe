<template>
  <div>
    <ul>
      <li v-for="food in foods" :key="food.id"> {{ food.name }} </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Foods',
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
