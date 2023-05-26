<template>
  <div class="hello">

    <div id="app">
      <el-card shadow="hover">
          <h3>评论词云图</h3>
          <wordcloud
          :data="defaultWords"
          nameKey="name"
          valueKey="value"
          :color="myColors"
          :showTooltip="true"
          :wordClick="wordClickHandler">
          </wordcloud>
      </el-card>

    </div>
  </div>
</template>
<script>
import wordcloud from 'vue-wordcloud'
import request from "@/utils/request";
export default {
    name: 'WordCloud',
    data() {
      return {
        myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
        defaultWords: [],
        business_id: JSON.parse(localStorage.getItem("user"))['id'],
      }
    },
    components: {
        wordcloud
    },
    created(){
        this.load()
    },
    methods: {
        load(){
            request.get("/business/wordcloud", {
            params: {
              business_id: this.business_id,
            }
          }).then(res => {
            console.log(res)

            this.defaultWords = res
            this.total = res.total

          })
        },
        wordClickHandler(name, value, vm) {
          console.log('wordClickHandler', name, value, vm);
        }
    },
}
</script>
<style>
.wordCloud{
    height: 500px !important;
    width: 900px !important;
    margin-left: 200px !important;
  }
</style>