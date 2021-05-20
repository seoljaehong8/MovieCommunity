<template>
  <div class="login">
    <h1>로그인</h1>
    <div>
      <label class="label" for="username">아이디</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <br>
    <div>
      <label class="label" for="password">비밀번호</label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <br>
    <router-link :to="{ name: 'Signup' }">회원이 아니신가요? </router-link> 
    <br>
    <br>
    <button class="btn btn-secondary" @click="login">로그인</button>

  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'MovieList' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  .login {
    margin: 0 auto;
    border: solid 3px gray;
    width: 300px;
  }

  .label {
    width: 70px;
  }
</style>