<template>
  <div>

    <div style="margin: 10px 0">
      <el-input style="width: 200px" placeholder="请输入部门" suffix-icon="el-icon-search" v-model="department"></el-input>
      <el-input style="width: 200px" placeholder="请输入面试者" suffix-icon="el-icon-message" class="ml-5" v-model="interviewee"></el-input>
      <el-input style="width: 200px" placeholder="请输入面试官" suffix-icon="el-icon-position" class="ml-5" v-model="interviewer"></el-input>
      <el-select v-model="state" class="ml-5" placeholder="选择状态">
        <el-option v-for="item in slist" :value="item.state" :key="item.state"
                   :label="item.content" style="font-weight: normal; color: #6b6b6b"></el-option>
      </el-select>
      <el-button class="ml-5" type="primary" @click="load">搜索</el-button>
      <el-button type="warning" @click="reset">重置</el-button>
    </div>


    <el-table :data="tableData" border stripe :header-cell-class-name="'headerBg'"  @selection-change="handleSelectionChange">
      <el-table-column prop="id" label="序号" align="center"></el-table-column>
      <el-table-column prop="time" label="时间" align="center"></el-table-column>
      <el-table-column prop="department" label="部门" align="center"></el-table-column>
      <el-table-column prop="interviewee" label="面试者" align="center"></el-table-column>
      <el-table-column prop="interviewer" label="面试官" align="center"></el-table-column>
      <el-table-column prop="state" label="状态" align="center">
        <template slot-scope="scope">
          <span v-if="scope.row.state==0">未预约</span>
          <span v-if="scope.row.state==1">已预约</span>
          <span v-if="scope.row.state==2">已完成</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
          <el-button type="success" @click="handleEdit(scope.row)">面试<i class="el-icon-edit"></i></el-button>
          <el-popconfirm
              class="ml-5"
              confirm-button-text='确定'
              cancel-button-text='我再想想'
              icon="el-icon-info"
              icon-color="red"
              title="您确定删除吗？"
              @confirm="del(scope.row.id)"
          >
            <el-button type="danger" slot="reference">删除 <i class="el-icon-remove-outline"></i></el-button>
          </el-popconfirm>
        </template>
      </el-table-column>
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

    <el-dialog title="面试信息" :visible.sync="dialogFormVisible" width="30%" >
      <el-form label-width="80px" size="small">
        <el-form-item label="姓名">
          <span>{{form.interviewee}}</span>
        </el-form-item>
        <el-form-item label="部门">
          <span>{{form.department}}</span>
        </el-form-item>
        <el-form-item label="简历">
          <span>{{form.cv}}</span>
        </el-form-item>
        <el-form-item label="问题">
          <el-select v-model="form.problem" placeholder="选择问题">
            <el-option v-for="prob in problems" :value="prob.content" :key="prob.problemID"
                       :label="prob.content" style="font-weight: normal; color: #6b6b6b"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="评语">
          <el-input v-model="form.evaluate"></el-input>
        </el-form-item>
        <el-form-item label="是否通过">
          <el-switch v-model="form.result"></el-switch>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Interview.vue",
  data() {
    return {
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: 5,
      id: "",
      interviewee: "",
      interviewer: "",
      department: "",
      time: "",
      form: {
        result: false
      },
      dialogFormVisible: false,
      multipleSelection: [],
      problems: [],
      user: JSON.parse(localStorage.getItem("user")),
      state: -1,
      slist: [{state: -1,content: "请选择状态"},{state: 0,content: "未预约"},{state: 1,content: "已预约"},{state: 2,content: "已完成"}],
    }
  },
  created() {
    // 请求分页查询数据
    this.load()
  },
  methods: {
    load() {
      request.get("/interview/page", {
        params: {
          pageNum: this.pageNum,
          pageSize: this.pageSize,
          interviewee: this.interviewee,
          interviewer: this.interviewer,
          department: this.department,
          state: this.state
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
</style>