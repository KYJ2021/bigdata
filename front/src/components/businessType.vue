<template>
  <div>
    <div style="margin: 10px 0">
      <el-select v-model="rankBy" class="ml-5" placeholder="选择排序规则">
        <el-option v-for="item in rlist" :value="item.value" :key="item.name"
                   :label="item.name" style="font-weight: normal; color: #6b6b6b"></el-option>
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
  name: "ReviewChange",
  data() {
    return {
      tableData: [],
      revBusinessId: "",
      user: JSON.parse(localStorage.getItem("user")),
      rankBy: "",
      rankContent: "",
      rlist: [{name:'入驻店铺数',value:'count'},{name:'评论数',value:'review_count'},{name:'打卡数',value:'check_count'}],
    }
  },
  created() {
    // 请求分页查询数据
    this.load()
  },
  methods: {
    load(){
      this.tableData=[]
      request.get("/admin/typeSort", {
        params: {
          rankBy: this.rankBy,
        }
      }).then(res => {
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
          text: "商户种类排名",
        },
        tooltip: {
          trigger: "axis",
        },
        yAxis: {
          inverse: true,
          type: "category",
          data: this.tableData.map(item => item.categories),
        },
        xAxis: {},
        series: [
          {
            realtimeSort: true,
            data: this.tableData.map(item => item[this.rankBy]),
            type: "bar",
            areaStyle:"#f70",
            label: {
                show: true,
                position: 'right'
            }
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