<template>
  <el-menu :default-openeds="['1', '3']" style="min-height: 100%; overflow-x: hidden"
           background-color="#364f6b"
           text-color=white
           active-text-color="#fc5185"
           :collapse-transition="false"
           :collapse="isCollapse"
           router
  >
    <div style="height: 60px; line-height: 60px; text-align: center">
      <img src="../assets/overtime.svg" alt="" style="width: 25px; position: relative; top: 5px; right: 5px">
      <b style="color: #f0f0f0" v-show="logoTextShow">点评推荐系统</b>
    </div>
    <el-menu-item index="/">
      <template slot="title">
        <i class="el-icon-s-home"></i>
        <span slot="title">主页</span>
      </template>
    </el-menu-item>
    <el-submenu v-if="businessVisible" index="2">
      <template slot="title">
        <i class="el-icon-menu"></i>
        <span slot="title">商户应用</span>
      </template>
      <el-menu-item index="/businessRank">
        <template slot="title">
          <i class="el-icon-question"></i>
          <span slot="title">商户排名</span>
        </template>
      </el-menu-item>
      <el-submenu index="2-1">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span slot="title">评论分析</span>
        </template>
        <el-menu-item index="/ReviewChange">
          <template slot="title">
            <i class="el-icon-alarm-clock"></i>
            <span slot="title">评论变化</span>
          </template>
        </el-menu-item>
        <el-menu-item index="/WordCloud">
          <template slot="title">
            <i class="el-icon-alarm-clock"></i>
            <span slot="title">评论词云</span>
          </template>
        </el-menu-item>
      </el-submenu>
      <el-menu-item index="/businessAdvice">
        <template slot="title">
          <i class="el-icon-s-custom"></i>
          <span slot="title">经营建议</span>
        </template>
      </el-menu-item>
    </el-submenu>
    <el-submenu v-if="adminVisible" index="3">
      <template slot="title">
        <i class="el-icon-menu"></i>
        <span slot="title">平台应用</span>
      </template>
      <el-submenu index="3-1">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span slot="title">用户分析</span>
        </template>
        <el-menu-item index="/NewUser">
          <template slot="title">
            <i class="el-icon-alarm-clock"></i>
            <span slot="title">用户新增</span>
          </template>
        </el-menu-item>
        <el-menu-item index="/UserActivity">
          <template slot="title">
            <i class="el-icon-alarm-clock"></i>
            <span slot="title">用户活跃度</span>
          </template>
        </el-menu-item>
      </el-submenu>
      <el-submenu index="3-2">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span slot="title">商户分析</span>
        </template>
        <el-menu-item index="/businessType">
          <template slot="title">
            <i class="el-icon-alarm-clock"></i>
            <span slot="title">各种类商户</span>
          </template>
        </el-menu-item>
        <el-menu-item index="/areaRank">
          <template slot="title">
            <i class="el-icon-alarm-clock"></i>
            <span slot="title">各地区商户</span>
          </template>
        </el-menu-item>
        <el-menu-item index="/brand">
          <template slot="title">
            <i class="el-icon-alarm-clock"></i>
            <span slot="title">连锁品牌</span>
          </template>
        </el-menu-item>
      </el-submenu>
    </el-submenu>
    <el-menu-item index="/booking" v-if="intervieweeVisible">
      <template>
        <i class="el-icon-s-promotion"></i>
        <span slot="title">预约面试</span>
      </template>
    </el-menu-item>
    <el-menu-item index="/results" v-if="intervieweeVisible">
      <template>
        <i class="el-icon-s-claim"></i>
        <span slot="title">查看结果</span>
      </template>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: "Aside.vue",
  props: {
    isCollapse: Boolean,
    logoTextShow: Boolean
  },
  data(){
    return{
      businessVisible: false,
      intervieweeVisible: false,
      adminVisible: false,
      user: {}
    }
  },
  created() {
    this.load()
    if(this.user.userType == 2){
      this.businessVisible=true
    }else if(this.user.userType ==1){
      this.intervieweeVisible=true
    }else if (this.user.userType ==0){
      this.adminVisible=true
    }
    console.log(typeof this.user.userType)
  },
  methods:{
    load(){
      this.user=JSON.parse(localStorage.getItem("user"))
    }
  }
}
</script>

<style scoped>

</style>