<template>
  <div id="app">
    <span>
      <i class="fas fa-film fa-3x"></i>
    </span>
      <h1 class="title">Movie World</h1>

    <div id="nav">
      <span v-if="isLogin">
        <router-link @click.native="logout" to="#">Logout</router-link> |
        <router-link :to="{ name: 'MovieList' }">Movie</router-link> |
        <router-link :to="{ name: 'ReviewList' }">Review</router-link> |
      </span>
      <span v-else>
        
        <!-- <router-link :to="{ name: 'Login' }">Login</router-link>  -->
      </span>
    </div>
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
  /* width: 100vw;
  height: 100vh; */
  
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.title {
  display: inline;
  margin-left: 10px;
  font-family: 'Mountains of Christmas', cursive;
}
</style>
