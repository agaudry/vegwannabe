<template>
  <div class='p-4 h-screen font-sans'>
    <NavBar v-bind:displayLogin="false"/>
    <div class="flex justify-center pt-20 pb-8 px-4">
      <button @click='toggleView()' class="flex-grow focus:outline-none mt-4 bg-pop bg-opacity-25 border-pop border border-opacity-100 px-2 py-1 text-light active:font-bold active:bg-opacity-0" type="button">Login</button>
      <button @click='toggleView()' class="flex-grow focus:outline-none mt-4 bg-pop bg-opacity-25 border-pop border border-opacity-100 px-2 py-1 text-light active:font-bold active:bg-opacity-0" type="button">Signup</button>
    </div>
    <div v-show="showLogin" id='login'>
        <div class="px-4 text-light">
          <div class="col-span-9 border-b border-pop">
            <input class="p-1 appearance-none bg-pop bg-opacity-25 text-pop focus:outline-none w-full" type='text' name='email' v-model='input.email' placeholder='Email' />
          </div>
          <div class="col-span-9 border-b border-pop">
            <input class="mt-4 p-1 appearance-none bg-pop bg-opacity-25 text-pop focus:outline-none w-full" type='password' name='password' v-model='input.password' placeholder='Password' />
          </div>
          <button @click='login()' class="focus:outline-none mt-4 rounded bg-light bg-opacity-50 border-light border border-opacity-100 px-2 py-1 text-dark font-bold" type='button'>Login</button>
        </div>
    </div>
    <div v-show="!showLogin" id='signup'>
      <div class="px-4 text-light">
          <div class="col-span-9 border-b border-pop">
            <input class="p-1 appearance-none bg-pop bg-opacity-25 text-pop focus:outline-none w-full" type='text' name='username' v-model='input.username' placeholder='Username' />
          </div>
          <div class="col-span-9 border-b border-pop">
            <input class="mt-4 p-1 appearance-none bg-pop bg-opacity-25 text-pop focus:outline-none w-full" type='text' name='email' v-model='input.email' placeholder='Email' />
          </div>
          <div class="col-span-9 border-b border-pop">
            <input class="mt-4 p-1 appearance-none bg-pop bg-opacity-25 text-pop focus:outline-none w-full" type='password' name='password' v-model='input.password' placeholder='Password' />
          </div>
          <button @click='signup()' class="focus:outline-none mt-4 rounded bg-light bg-opacity-50 border-light border border-opacity-100 px-2 py-1 text-dark font-bold" type='button'>Signup</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import NavBar from './NavBar.vue'

export default {
  name: 'Login',
  components: {
    NavBar,
  },
  data() {
    return {
      cookie: document.cookie,
      showLogin: true,
      input: {
        username: '',
        email: '',
        password: ''
      },
      confirmation: ''
    }
  },
  methods: {
    toggleView() {
      this.showLogin = !this.showLogin
    },
    login() {
      const path = '/auth/login'
      const payload = { email: this.input.email, password: this.input.password }
      axios.post(path, payload)
        .then((res) => {
          document.cookie = `token=${res.data.access_token}; max-age=1209600; path='/'`
          this.$router.push('/')
        })
    },
    signup() {
      const path = '/auth/signup'
      const payload = { username: this.input.username, email: this.input.email, password: this.input.password }
      axios.post(path, payload)
        .then(() => {
          this.login()
        })
    },
  }
}
</script>
