<template>
  <div>
    <img v-if="imageData" :src="imageData" />
    <button @click="loadPlot">加载图表</button>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
    name: "businessRank",
  data() {
    return {
      imageData: null,
    }
  },
  methods: {
    loadPlot() {
      request.get("/api/plot")
        .then(res => {
          this.imageData = 'data:image/png;base64,' + res.image
        })
        .catch(error => {
          console.error(error)
        })
    },
  },
}
</script>

<style scoped>

</style>