<template>
  <div>
    <h1>Recommend</h1>
    <div class="container">
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

        <div class="content content_1">액션</div>
        <div class="content content_2">공포</div>
        <div class="content content_3">스릴러</div>
        <div class="content content_4">드라마</div>
        <div class="content content_5">코미디</div>
        <div class="content content_6">SF</div>
      </div>
      <button @click="onClickTrigger" class="trigger">뽑기</button>
    </div>
  </div>
</template>

<script>



export default {
  name: 'Recommend',
  methods: {
    onClickTrigger: function(e) {
      const roulette = document.querySelector(".roulette");
      roulette.setAttribute('style','animation: rotation 7s ease-in-out forwards;')
      // roulette.classList.add("loop");
    },
  }
  
}
</script>

<style>
.fill {
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
  font-size: 30px;
  font-weight: bold;
  padding-top: 30px;
  height: 370px;
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
  width: 400px;
  height: 3px;
  background: black;
  position: absolute;
  top: 200px;
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
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background: white;
  border: 3px solid black;
  position: relative;
}
.roulette.loop {
  animation: rotation 7s ease-in-out forwards;
}
</style>