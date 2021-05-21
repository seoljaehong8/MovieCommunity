<template>
  <div class="signup">
    <h1>회원가입</h1>
    <div>
      <label class="" for="username">아이디 </label>
      <input type="text" id="username" v-model="credentials.username">
      
    </div>
    <br>
    <div>
      <label class="label" for="password">비밀번호 </label>
      <input type="password" id="password" v-model="credentials.password">
      
    </div>
    <br>
    <div>
      <label class="label" for="passwordConfirmation">비밀번호 재확인 </label>
      <input class="" type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <br>
    <button class="btn btn-outline-secondary" @click="signup(credentials)">가입하기</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/signup/`,
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  .signup {
    margin: 0 auto;
    width: 300px;
    padding: 50px;
    border-radius: 30px;
    background-color: #F6F6F6;
    font-family: 'Noto Sans KR', sans-serif;
  }


 


</style>