import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'
import ReviewList from '@/views/reviews/ReviewList'
import ReviewForm from '@/components/reviews/ReviewForm'
import ReviewDetail from '@/components/reviews/ReviewDetail'
import movieDetail from '@/components/movies/MovieDetail'



Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies/movieList',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/reviews/reviewList',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/reviews/reviewForm',
    name: 'ReviewForm',
    component: ReviewForm,
  },
  {
    path: '/reviews/reviewDetail',
    name: 'ReviewDetail',
    component: ReviewDetail,
    props: true
  },
  {
    path: '/movies/movieDetail',
    name: 'movieDetail',
    component: movieDetail,
    props: true
  }


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
