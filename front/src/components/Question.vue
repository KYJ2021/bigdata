<template>
  <div>
    <!--搜索栏,重置和搜索方法未写-->
    <div style="margin: 10px 0">
      <el-button type="primary" slot="reference" @click="handleAdd"><i class="el-icon-circle-plus-outline"></i>新增</el-button>
    </div>
    <!--    //搜索栏结果-->
    <div>
      <el-table :data="tableData" border stripe :header-cell-class-name="'headerBg'"  @selection-change="handleSelectionChange">
        <el-table-column prop="id" label="ID" align="center"></el-table-column>
        <el-table-column prop="content" label="内容" align="center"></el-table-column>
        <el-table-column prop="department" label="部门" align="center"></el-table-column>
        <el-table-column label="操作" align="center">
          <template slot-scope="scope">
            <el-button type="primary" slot="reference" @click="handleEdit(scope.row)">编辑</el-button>
            <el-button type="danger" slot="reference" @click="handleDel(scope.row)">删除</el-button>
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
    <el-dialog :visible.sync="dialogFormVisible" width="30%" >
      <span>确认是否删除</span>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="danger" @click="del">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="addVisible" width="30%" title="问题">
      <el-form label-width="80px" size="small" :model="depform" :rules="rules" ref="quesForm">
        <el-form-item label="选择部门" prop="departmentId">
          <el-select v-model="depform.departmentId" placeholder="选择部门">
            <el-option v-for="dep in deps" :value="dep.departmentID" :key="dep.departmentID"
                       :label="dep.departmentName" style="font-weight: normal; color: #6b6b6b"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="输入问题" prop="content">
          <el-input size="medium" style="margin: 10px 0" v-model="depform.content"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="cancel">取 消</el-button>
        <el-button type="primary" @click="add">确 定</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Question",
  data() {
    return {
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: 5,
      time: "0000-00-00 HH:mm:ss",
      form: {},
      dialogFormVisible: false,
      multipleSelection: [],
      addVisible: false,
      editVisible: false,
      user: JSON.parse(localStorage.getItem("user")),
      deps: [],
      depform: {},
      rules: {
        departmentId: [
          { required: true, message: '请选择部门', trigger: 'change' },
        ],
        content: [
          { required: true, message: '请输入问题', trigger: 'blur' },
        ],
      }
    }
  },
  created() {
    this.load()
  },
  methods:{
    load(){
      request.get("/problem/page", {
        params: {
          pageNum: this.pageNum,
          pageSize: this.pageSize,
        }
      }).then(res => {
        console.log(res)

        this.tableData = res.records
        this.total = res.total

      })
      request.get("/department").then((res)=>{
        this.deps=res
      })
      this.form={}
      this.depform={}
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
    handleDel(row) {
      this.form = row
      this.dialogFormVisible = true
    },
    handleAdd() {
      this.addVisible=true
    },
    handleEdit(row){
      this.depform =row
      this.addVisible = true
    },
    del(){
      request.delete("/problem/" + this.form.id).then(res => {
        if (res) {
          this.dialogFormVisible = false
          this.$message.success("删除成功")
          this.load()
        } else {
          this.$message.error("删除失败")
        }
      })
    },
    add(){
      this.$refs['quesForm'].validate((valid) => {
        if (valid) {
          request.post("/problem/save", this.depform).then(res => {
            if (res) {
              this.$message.success("保存成功")
              this.addVisible = false
              this.load()
            } else {
              this.$message.error("保存失败")
            }
          })
        }
      })
    },
    cancel(){
      this.addVisible = false
      this.form={}
      this.depform={}
    }
  }
}
</script>

<style scoped>

</style>