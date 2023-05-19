<template>
  <div id="app">
    <Recommendation />
  </div>
</template>

<script>
import Recommendation from './components/Recommendation.vue';

export default {
  name: 'App',
  components: {
    Recommendation,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>