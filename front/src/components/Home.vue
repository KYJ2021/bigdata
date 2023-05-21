<template>
  <div>
    <div style="margin: 150px 700px">
      <img v-if="getTimeState()==0" src="../assets/undraw_home_run_re_pogc.svg" alt="" style="width: 450px; position: relative; top: 50px; right: 5px">
      <img v-if="getTimeState()==1" src="../assets/undraw_beach_day_cser.svg" alt="" style="width: 400px; position: relative; top: 5px; right: 5px">
      <img v-if="getTimeState()==2" src="../assets/undraw_ready_for_waves_vlke.svg" alt="" style="width: 350px; position: relative; top: 50px; right: 5px">
      <img v-if="getTimeState()==3" src="../assets/undraw_cat_re_gkh9.svg" alt="" style="width: 400px; position: relative; top: 200px; right: 5px">
    </div>
  </div>
</template>

<script>
export default {
  name: "Home.vue",
  methods:{
    getTimeState(){
// 获取当前时间
      let timeNow = new Date();
// 获取当前小时
      let hours = timeNow.getHours();
// 设置默认文字
      let state= -1;
// 判断当前时间段
      if (hours >= 0 && hours <= 10) {
        state = 0;
      } else if (hours > 10 && hours <= 14) {
        state= 1;
      } else if (hours > 14 && hours <= 18) {
        state= 2;
      } else if (hours > 18 && hours <= 24) {
        state= 3;
      }
      return state;
    },
  }
}

</script>

<style scoped>

</style>