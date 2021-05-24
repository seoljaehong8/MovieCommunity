<template>
  <div>
    <span style="font-size:120px; color:white;">
      <i class="far fa-hand-point-down"></i>
    </span>
    <div class="container">
      <div class="row">
        <div class="offset-3 col">
          <div class="roulette">
            <div class="fill fill_1"></div>
            <div class="fill fill_2"></div>
            <div class="fill fill_3"></div>
            <div class="fill fill_4"></div>
            <div class="fill fill_5"></div>
            <div class="fill fill_6"></div>

            <div class="line line_1"></div>
            <div class="line line_2"></div>
            <div class="line line_3"></div>
            <div class="line line_4"></div>

            <div v-for="(genre,idx) in getGenreList" :key="idx">
              <div :class="[content, contents[idx]]">{{genre}}</div>
            </div>
          </div>    
        </div>
      </div>
    </div>
    <div v-if="isStop">
      <button @click="onClickTrigger" class="trigger mt-5">다시</button>
    </div>
    <div v-else>
      <button @click="onClickTrigger" class="trigger mt-5">뽑기</button>

    </div>
    {{ getGenreList }}
    <h1 v-if="isStop" class="animate__animated animate__bounceInLeft" style="color:white;">{{getGenreList[2]}}</h1>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Recommend',
  data: function(){
    return {
      content: 'content',
      contents: ['content_1','content_2',
      'content_3','content_4','content_5','content_6'],
      isStop: false,
    }
  },
  computed: {
    getGenreList: function() {
      const genreList = [
        '액션','어드벤처','애니메이션','코미디','범죄','다큐멘터리','드라마',
        '가족','판타지','역사','공포','음악','미스테리','로맨스',
        'SF','TV영화','스릴러','전쟁','서부'
      ]
      const randeomGenre = _.sampleSize(genreList,6)
      return randeomGenre
    }
  },
  methods: {
    onClickTrigger: function() {
      const roulette = document.querySelector(".roulette");
      if (this.isStop){
        window.location.reload()
      }else {
        roulette.classList.add("loop");
        setTimeout(() => {
          this.isStop = true
        },7000)
      }
    },
  }
  
}
</script>

<style>
/* .fill {  
  position: absolute;
  top: 0;
  left: 0;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  clip: rect(0px, 400px, 400px, 200px);
}
.fill::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  clip: rect(0px, 200px, 400px, 0px);
  transform: rotate(60deg);
} */
.fill {  
  position: absolute;
  top: 0;
  left: 0;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  clip: rect(0px, 600px, 600px, 300px);
  z-index: 1;
}
.fill::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  clip: rect(0px, 300px, 600px, 0px);
  transform: rotate(60deg);
  z-index: 1;
}
.fill_1::after {
  background: lightcoral;
}
.fill_2 {
  transform: rotate(60deg);
}
.fill_2::after {
  background: lightgreen;
}
.fill_3 {
  transform: rotate(120deg);
}
.fill_3::after {
  background: lightblue;
}
.fill_4 {
  transform: rotate(180deg);
}
.fill_4::after {
  background: lightgray;
}
.fill_5 {
  transform: rotate(240deg);
}
.fill_5::after {
  background: lightsalmon;
}
.fill_6 {
  transform: rotate(300deg);
}
.fill_6::after {
  background: lightseagreen;
}
.content {
  z-index: 1;

  font-size: 30px;
  font-weight: bold;
  padding-top: 40px;
  height: 600px;
  position: absolute;
  width: 100%;
  text-align: center;
}
.content_1 {
  transform: rotate(35deg);
}
.content_2 {
  transform: rotate(95deg);
}
.content_3 {
  transform: rotate(150deg);
}
.content_4 {
  transform: rotate(207deg);
}
.content_5 {
  transform: rotate(265deg);
}
.content_6 {
  transform: rotate(330deg);
}
.line {
  z-index: 1;

  width: 600px;
  height: 3px;
  background: black;
  position: absolute;
  top: 300px;
  left: 0;
}
.line_1 {
  transform: rotate(90deg);
}
.line_2 {
  transform: rotate(150deg);
}
.line_3 {
  transform: rotate(210deg);
}
.line_4 {
  transform: rotate(270deg);
}
@keyframes rotation {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(7045deg);
  }
}
.roulette {
  width: 600px;
  height: 600px;
  border-radius: 50%;
  background: null;
  border: 3px solid black;
  position: relative;
}
.roulette.loop {
  animation: rotation 7s ease-in-out forwards;
}
</style>