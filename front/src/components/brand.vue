<template>
  <div>
    <div style="margin: 10px 0">
      <el-select v-model="tableType" class="ml-5" placeholder="选择图表类型">
        <el-option v-for="item in tlist" :value="item.value" :key="item.name"
                   :label="item.name" style="font-weight: normal; color: #6b6b6b" @click.native="choose_get_which"></el-option>
      </el-select>
      <el-select v-model="rankBy" class="ml-5" placeholder="选择查询规则" :disabled="whichEnable">
        <el-option v-for="item in rlist" :value="item[tableType]" :key="item[tableType]"
                   :label="item[tableType]" style="font-weight: normal; color: #6b6b6b"></el-option>
      </el-select>
      <el-button class="ml-5" type="primary" @click="load" round>筛选</el-button>
    </div>
    <div>
      <el-card shadow="hover">
        <div ref="chart" style="height: 400px;"></div>
      </el-card>
    </div>
  </div>

</template>

<script>
import request from "@/utils/request";
import * as echarts from "echarts";


export default {
  name: "brand",
  data() {
    return {
      tableData: [],
      revBusinessId: "",
      user: JSON.parse(localStorage.getItem("user")),
      tableType: "",
      rankBy: "",
      rankContent: "",
      rlist: [],
      tlist: [{name:'所有',value:'all'},{name:'城市',value:'city'},{name:'州',value:'state'}],
        whichEnable: true,
    }
  },
  created() {

  },
  methods: {
    load(){
      this.tableData=[]
      request.get("/admin/brand"+this.tableType, {
        params: {
          rankBy: this.rankBy,
        }
      }).then(res => {
        console.log(res.records)
        this.tableData = res.records
        this.renderChart()
      })
    },
      get_all_state(){
        request.get("/admin/allstate").then(res =>{
            this.rlist=res.records
        })
      },
      get_all_city(){
        request.get("/admin/allcity").then(res =>{
            this.rlist=res.records
        })
      },
      choose_get_which(){
        if(this.tableType=="all"){
            this.whichEnable=true
            this.rankBy=""
        }
        else if (this.tableType=="city"){
            this.get_all_city()
            this.rankBy=""
            this.whichEnable=false
        }
        else if (this.tableType=="state"){
            this.get_all_state()
            this.rankBy=""
            this.whichEnable=false
        }
        else {
            console.log("error")
        }
      },
    // 渲染图表
    renderChart() {
      const chart = echarts.init(this.$refs.chart)
      const data = this.tableData.map(item => ({ name: item.name, value: item.value }))
      const option = {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          data: data.map(item => item.name)
        },
        series: [
          {
            name: 'Fruit',
            type: 'pie',
            radius: '50%',
            data: data.sort((a, b) => a.value - b.value),
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
      chart.setOption(option)
    }
  },
};
</script>

<style scoped>

</style>