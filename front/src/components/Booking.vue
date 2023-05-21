<template>
  <div>
<!--搜索栏,重置和搜索方法未写-->
<!--    //搜索栏结果-->
    <div>
      <el-table :data="tableData" border stripe :header-cell-class-name="'headerBg'"  @selection-change="handleSelectionChange">
        <el-table-column prop="time" label="时间" align="center"></el-table-column>
        <el-table-column label="操作" align="center">
          <template slot-scope="scope">
            <el-button type="primary" slot="reference" @click="handleEdit(scope.row)">预约</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
<!--    //分页-->
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
      <el-form label-width="80px" size="small" :model="form" :rules="rules" ref="bookForm">
        <el-form-item label="部门" prop="departmentId">
          <el-select v-model="form.departmentId" placeholder="选择意向部门">
            <el-option v-for="dep in deps" :value="dep.departmentID" :key="dep.departmentID"
                       :label="dep.departmentName" style="font-weight: normal; color: #6b6b6b"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="简历" prop="cv">
          <el-input v-model="form.cv"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="book">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Booking",
  data() {
    return {
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: 5,
      time: "0000-00-00 HH:mm:ss",
      form: {
        intervieweeId: ""
      },
      depform:{
        departmentID: "",
        department: ""
      },
      depSelect:{},
      dialogFormVisible: false,
      multipleSelection: [],
      visible: false,
      user: JSON.parse(localStorage.getItem("user")),
      deps:[],
      selectDepId: 0,
      state: 0,
      rules: {
        departmentId: [
          { required: true, message: '请选择部门', trigger: 'change' },
        ],
        cv: [
          { required: true, message: '请输入简历', trigger: 'blur' },
        ],
      }
    }
  },
  created() {
    this.load()
  },
  methods:{
    load(){
      request.get("/interview/page", {
        params: {
          pageNum: this.pageNum,
          pageSize: this.pageSize,
          state: this.state
        }
      }).then(res => {
        console.log(res)

        this.tableData = res.records
        this.total = res.total

      })
      request.get("/department").then((res)=>{
        this.deps=res
      })
    },
    reset() {
      this.username = ""
      this.email = ""
      this.address = ""
      this.load()
    },
    handleSelectionChange(val) {
      console.log(val)
      this.multipleSelection = val
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
    },
    handleEdit(row) {
      var d1=new Date(Date.parse((row.time).replace(/-/g,"/")))
      var d2=new Date()
      console.log(d1)
      if(d1>d2){
        this.form = row
        this.dialogFormVisible = true
      }else {
        this.$message.error("已过期")
      }
    },
    book(){
      this.$refs['bookForm'].validate((valid)=>{
        if (valid){
          this.form.intervieweeId=this.user.id
          this.form.state=1
          request.post("/interview/save", this.form).then(res => {
            if (res) {
              this.$message.success("保存成功")
              this.dialogFormVisible = false
              this.load()
            } else {
              this.$message.error("保存失败")
            }
          })
        }
      })
    },
  }
}
</script>

<style scoped>

</style>