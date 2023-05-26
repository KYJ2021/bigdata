<template>
  <div>
    <div style="margin: 10px 0">
      <el-select v-model="which_year" class="ml-5" placeholder="年份">
        <el-option v-for="item in dlist" :value="item" :key="item"
                   :label="item" style="font-weight: normal; color: #6b6b6b"></el-option>
      </el-select>
      <el-button class="ml-5" type="primary" @click="load" round>筛选</el-button>
    </div>

    <el-table :data="tableData" @selection-change="handleSelectionChange">
      <el-table-column prop="rev_user_id" label="用户id" align="center"></el-table-column>
      <el-table-column prop="year" label="年份" align="center"></el-table-column>
      <el-table-column prop="count" label="活跃度（相对值）" align="center" i class="el-icon-star"></el-table-column>
    </el-table>

    <div style="padding: 10px 0">
      <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="pageNum"
          :page-sizes="[5, 10, 20, 50]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
      </el-pagination>
    </div>


  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "UserActivity",
  data() {
    return {
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: 10,
      categories: "请选择种类",
      orderBy: "",
      user: JSON.parse(localStorage.getItem("user")),
      categories_array: JSON.parse(localStorage.getItem("user"))['categories'].split(',').map((item) => item.trim()),
      //这块变量名要改成和数据库中的一致
      isLocal: 0,
      rankRule: 0,
      Llist: [{isLocal: 0,content: "当前地区"},{isLocal: 1,content: "全部地区"}],
      slist: [{rankRule: 0,content: "综合"},{rankRule: 1,content: "按评论数"},{rankRule: 2,content: "按打卡数"}],
      dlist: ['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
      which_year: '2022',
      city: 'Philadelphia',
    }
  },
  created() {
    // 请求分页查询数据
    this.load()
  },
  methods: {
    load() {
      console.log(this.categories_array)
      this.tableData=[]
      request.get("/admin/activity", {
        params: {
          pageNum: this.pageNum,
          pageSize: this.pageSize,
          which_year: this.which_year
        }
      }).then(res => {
        console.log(res)

        this.tableData = res.records
        this.total = res.total

      })
    },
    save() {
      if(this.form.state==1){
        this.form.state=2
        this.form.interviewerId=this.user.id
      }
      request.post("/interview/save", this.form).then(res => {
        if (res) {
          this.$message.success("保存成功")
          this.dialogFormVisible = false
          this.load()
        } else {
          this.$message.error("保存失败")
        }
      })
    },
    handleAdd() {
      this.dialogFormVisible = true
      this.form = {}
    },
    handleEdit(row) {
      if(row.state!=0){
        this.form = row
        this.dialogFormVisible = true
        request.get("/problem/"+this.form.departmentId).then((res)=>{
          this.problems=res
        })
      }
      else {
        this.$message.error("未预约")
      }
    },
    del(id) {
      request.delete("/interview/" + id).then(res => {
        if (res) {
          this.$message.success("删除成功")
          this.load()
        } else {
          this.$message.error("删除失败")
        }
      })
    },
    handleSelectionChange(val) {
      console.log(val)
      this.multipleSelection = val
    },
    delBatch() {
      let ids = this.multipleSelection.map(v => v.id)  // [{}, {}, {}] => [1,2,3]
      request.post("/user/del/batch", ids).then(res => {
        if (res) {
          this.$message.success("批量删除成功")
          this.load()
        } else {
          this.$message.error("批量删除失败")
        }
      })
    },
    reset() {
      this.department = ""
      this.interviewer = ""
      this.interviewee = ""
      this.state = -1
      this.load()
    },
    handleSizeChange(pageSize) {
      console.log(pageSize)
      this.pageSize = pageSize
      this.load()
    },
    handleCurrentChange(pageNum) {
      console.log(pageNum)
      this.pageNum = pageNum
      this.load()
    }
  }
}
</script>

<style>
.headerBg {
  background: #eee!important;
}
.my-table-row {
  margin-bottom: 20px;
}
</style>