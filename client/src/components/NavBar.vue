<template>
    <header>
        <div class="px-5 flex justify-between items-center">
            <div class="py-2 text-3xl font-bold text-center text-light">
                <a href="#" @click="goTo('/')">Vegwannabe</a>
            </div>
            <div v-if="displayLogin">
              <div v-if="!user">
                <a href="#" @click="goTo('login')" class="py-2 text-md text-pop text-opacity-75 hover:text-opacity-100">Login</a>
              </div>
              <div v-else>
                <a href="#" @click="goTo('login')" class="py-2 px-2 text-sm text-pop text-opacity-75 hover:text-opacity-100">{{ user }}</a>
                <button @click="isOpen = !isOpen" type="button" class="focus:outline-none text-pop text-opacity-75 hover:text-opacity-100">
                  <svg class="h-2 w-3 fill-current" viewBox="0 0 512.011 512.011">
                    <path v-if="!isOpen" d="M505.755,123.592c-8.341-8.341-21.824-8.341-30.165,0L256.005,343.176L36.421,123.592c-8.341-8.341-21.824-8.341-30.165,0s-8.341,21.824,0,30.165l234.667,234.667c4.16,4.16,9.621,6.251,15.083,6.251c5.462,0,10.923-2.091,15.083-6.251l234.667-234.667C514.096,145.416,514.096,131.933,505.755,123.592z"/>
                    <path v-if="isOpen" d="M492,236H20c-11.046,0-20,8.954-20,20c0,11.046,8.954,20,20,20h472c11.046,0,20-8.954,20-20S503.046,236,492,236z"/>
                  </svg>
                </button>
              </div>
            </div>
        </div>
        <div v-if="isOpen" class="rounded-sm mx-4 bg-light bg-opacity-75 text-dark text-right font-semibold">
            <a href="#" @click="goTo('about')" class="rounded block px-4 pt-2 pb-1 hover:bg-light focus:bg-light">About</a>
            <a href="#"  @click="goTo('display_foods')" class="rounded block px-4 pb-2 pt-1 hover:bg-light focus:bg-light">Food diary</a>
            <a href="#"  @click="logout()" class="rounded block px-4 pb-2 pt-1 hover:bg-light focus:bg-light">Logout</a>
        </div>
    </header>
</template>

<script>
import axios from 'axios'

export default {
  name: 'NavBar',
  props: ['displayLogin'],
  data() {
    return {
      isOpen: false,
      user: null
    }
  },
  methods: {
    goTo(route) {
      this.$router.push(route)
    },
    getUser(cookie) {
      const token = cookie.split('=')[1]
      const path = '/auth/user'
      const headers = { headers: { 'Authorization': `JWT ${token}` } }
      axios.get(path, headers)
        .then((res) => { this.user = res.data })
    },
    logout() {
      // const path = '/auth/logout'
      // const payload = this.user
      // const headers = { headers: { 'Authorization': `JWT ${token}` } }
      // axios.post(path, payload, headers)
      this.user = null
      document.cookie = "token=; max-age=0; path='/'"
      this.$router.push('/')
    }
  },
  created() {
    if (document.cookie) {
      this.getUser(document.cookie)
    }
  }
}
</script>
