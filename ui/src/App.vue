<template>
  <div class="app">
    <MainPage />
  </div>
</template>

<script>
import MainPage from "@/components/MainPage.vue";

export default {
  name: "App",
  components: {
    MainPage,
  },
};
</script>

<style>
.app {
  width: 100%;
  height: 100%;
}
</style>