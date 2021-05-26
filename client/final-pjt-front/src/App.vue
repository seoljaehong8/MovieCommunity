<template>
  <div>
    <div id="app">
      <nav v-if="isLogin" class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid">
          <a class="navbar-brand text-red" href="/movies/movieList">
            <span>
              <i class="fas fa-film fa-3x" style="font-size:30px;"></i>
            </span>
              <h3 class="title">Pick Screen</h3>
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
              <li class="nav-item">
                <router-link class="text-white-my" :to="{ name: 'MovieList' }">Movie</router-link>
              </li>
              <li class="nav-item">
                <router-link class="text-white-my" :to="{ name: 'ReviewList' }">Review</router-link>
              </li>
              <li class="nav-item">
                <router-link class="text-white-my" :to="{ name: 'Recommend' }">Pick!!!</router-link>
              </li>
              <!-- <li class="nav-item">
                <router-link class="text-white-my" :to="{ name: 'Profile' }">Profile</router-link>
              </li> -->
              <li class="nav-item">
                <router-link class="text-white-my" @click.native="logout" to="#">Logout</router-link>
              </li>

            </ul>
          </div>
        </div>
      </nav>

      <span v-else>

      </span>

      <div style="padding-top:100px;">
        <router-view @login="isLogin = true"/>

      </div>
    </div>

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
    },

  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    } else if(this.$route.path !== '/accounts/login') {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style scoped>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
  /* width: 100vw;
  height: 100vh; */
  
}
.title {
  display: inline;
  margin-left: 10px;
  font-family: 'Mountains of Christmas', cursive;
}

 .navbar{
   background-color:rgb(15, 15, 15);
   margin-bottom:50px;
   position: fixed;
   z-index:10;
   width:100%;
 }
 .text-white-my{
   color:rgb(173, 173, 173);
   text-decoration: none;
   margin-right:15px;
   padding-top:0px;
 }
 .text-white-my:hover{
   color:white;
 }
 .text-red{
   color:red;
 }
 .nav-item{
   padding-top:15px;
 }
 .login{
   margin-top:100px;
 }
 .router-link-exact-active{
   color:white;
   font-size:20px;
 }
</style>
