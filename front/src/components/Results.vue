<template>
  <div style="margin: 100px auto; ">
    <div style="position: center">
      <el-col>
        <el-result icon="success" title="已通过" v-if="whetherPass">
          <template slot="extra">
              <el-button type="primary" size="medium" @click="logout">退出</el-button>
          </template>
        </el-result>
        <el-result icon="fail" title="再接再厉" v-if="whetherPass==false">
          <template slot="extra">
            <el-button type="primary" size="medium" @click="logout">退出</el-button>
          </template>
        </el-result>
      </el-col>
    </div>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Results",
  data() {
    return {
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: 2,
      username: "",
      email: "",
      address: "",
      form: {},
      dialogFormVisible: false,
      multipleSelection: [],
      whetherPass: false,
      user: JSON.parse(localStorage.getItem("user"))
    }
  },
  created() {
    this.check()
  },
  methods:{
    handleSizeChange(pageSize) {
      console.log(pageSize)
      this.pageSize = pageSize
      this.load()
    },
    handleCurrentChange(pageNum) {
      console.log(pageNum)
      this.pageNum = pageNum
      this.load()
    },
    handleSelectionChange(val) {
      console.log(val)
      this.multipleSelection = val
    },
    logout() {
      this.$router.push("/login")
      localStorage.removeItem("user")
      this.$message.success("退出成功")
    },
    check(){
      request.get("/interview/" +this.user.id).then(res => {
        if (res) {
          this.whetherPass=true
        } else {
          this.whetherPass=false
        }
      })
    }
  }
}
</script>

<style scoped>

</style>