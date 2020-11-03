<template>
    <header>
        <div class="px-5 flex justify-between">
            <div class="py-2 text-3xl font-bold text-center text-light">
                <a href="#" @click="goTo('/')">Vegwannabe</a>
            </div>
            <button @click="isOpen = !isOpen" type="button" class="focus:outline-none text-pop text-opacity-75 hover:text-opacity-100">
                <svg class="h-5 w-5 fill-current" viewBox="0 0 24 24">
                    <path v-if="!isOpen" d="M24 6h-24v-3h24v4zm0 5h-24v3h24v-4zm0 8h-24v3h24v-4z"/>
                    <path v-if="isOpen" d="M23.954 21.03l-9.184-9.095 9.092-9.174-2.832-2.807-9.09 9.179-9.176-9.088-2.81 2.81 9.186 9.105-9.095 9.184 2.81 2.81 9.112-9.192 9.18 9.1z"/>
                </svg>
            </button>
        </div>
        <div v-if="isOpen" class="rounded-sm mx-4 bg-light bg-opacity-75 text-dark text-right font-semibold">
            <a href="#" @click="goTo('about')" class="rounded block px-4 pt-2 pb-1 hover:bg-light focus:bg-light">About</a>
            <a href="#"  @click="goTo('display_foods')" class="rounded block px-4 pb-2 pt-1 hover:bg-light focus:bg-light">Food diary</a>
        </div>
    </header>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      isOpen: false
    }
  },
  methods: {
    goTo(route) {
      this.$router.push(route);
    }
  }
}
</script>
