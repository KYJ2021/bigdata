<template>
  <div>
    <el-card shadow="hover">
      <div ref="chart" style="height: 400px;"></div>
    </el-card>
  </div>
</template>

<script>
import request from "@/utils/request";
import * as echarts from "echarts";


export default {
  name: "NewUser",
  data() {
    return {
      tableData: [],
      revBusinessId: "",
      user: JSON.parse(localStorage.getItem("user"))
    }
  },
  created() {
    // 请求分页查询数据
    this.load()
  },
  methods: {
    load(){
      this.revBusinessId=this.user.id
      request.get("/admin/newUser").then(res => {
        console.log(res)
        this.tableData = res.records
        this.renderChart()
      })
    },
    // 渲染图表
    renderChart() {
      const chart = echarts.init(this.$refs.chart);

      // 配置项
      const option = {
        title: {
          text: "用户年度新增",
        },
        tooltip: {
          trigger: "axis",
        },
        xAxis: {
          type: "category",
          data: this.tableData.map(item => item.year),
        },
        yAxis: {},
        series: [
          {
            data: this.tableData.map(item => item.count),
            type: "line",
            areaStyle:"#f70"
          },
        ],
      };
      chart.setOption(option);
    },
  },
};
</script>

<style scoped>

</style>