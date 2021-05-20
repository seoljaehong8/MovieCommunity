<template>
  <div class="border row mb-3">
    <h1>회원가입</h1>
    <div>
      <label class="label" for="username">아이디 </label>
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
      <input class="inputPassword" type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <br>
    <button @click="signup(credentials)">가입하기</button>
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
  .title {
    
  }

  .border {
    margin: 0 auto;
    height: 400px;
    width: 300px;
    border: 3px solid gold
  }

  .label {
    width: 70px;
  }

  .inputPassword {
    margin-bottom: 50px;
  }
  /* 비밀번호 재확인 input 태그 위치 */


</style>