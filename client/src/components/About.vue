<template>
  <div class="p-4 h-screen font-sans">
    <NavBar v-bind:displayLogin="true"/>
    <h1>About</h1>
  </div>
</template>

<script>

import NavBar from './NavBar.vue'

export default {
  name: 'About',
  components: {
    NavBar,
  },
}
</script>
