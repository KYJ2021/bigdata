<template>
  <div>
    <!--搜索栏,重置和搜索方法未写-->
    <div style="margin: 10px 0">
      <el-button type="primary" @click="handleadd"><i class="el-icon-circle-plus-outline"></i>新增</el-button>
    </div>
    <!--    //搜索栏结果-->
    <div>
      <el-table :data="tableData" border stripe :header-cell-class-name="'headerBg'"  @selection-change="handleSelectionChange">
        <el-table-column prop="department" label="部门" align="center"></el-table-column>
        <el-table-column prop="time" label="时间" align="center"></el-table-column>
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
    <el-dialog :visible.sync="delFormVisible" width="30%" >
      <span>确认是否删除</span>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="delFormVisible = false">取 消</el-button>
        <el-button type="danger" @click="del">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="addFormVisible" width="30%" title="新增场次">
      <el-form>
        <el-form label-width="80px" size="small" :model="timeForm" :rules="rules" ref="timeForm">
          <el-form-item label="选择时间" prop="time">
              <el-date-picker
                  v-model="timeForm.time"
                  type="datetime"
                  :picker-options="endDateOpt"
                  placeholder="选择日期时间"
                  value-format="yyyy-MM-dd HH:mm:ss">
              </el-date-picker>
          </el-form-item>
        </el-form>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="cancel">取 消</el-button>
        <el-button type="danger" @click="add">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Arrangement",
  data() {
    return {
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: 5,
      time: "0000-00-00 HH:mm:ss",
      form: {},
      delFormVisible: false,
      multipleSelection: [],
      visible: false,
      user: JSON.parse(localStorage.getItem("user")),
      addFormVisible: false,
      timeForm: {},
      rules: {
        time: [
          { required: true, message: '请选择时间', trigger: 'change' },
        ],
      },
      endDateOpt: {
        disabledDate: (time) => {
          // 日期选择限制
          let oneDay = 60 * 60 * 24 * 1000;
          return time.getTime() < Date.now() - oneDay;
        },
        // selectableRange 用来限制时分秒的选择，这里要求只能选择当前时间之后到0点的时间点
        selectableRange: `${Date().split(" ")[4]} - 23:59:59`,
      },
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
        }
      }).then(res => {
        console.log(res)

        this.tableData = res.records
        this.total = res.total

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
    handleDel(row) {
      this.form = row
      this.delFormVisible = true
    },
    del(){
      request.delete("/interview/" + this.form.id).then(res => {
        if (res) {
          this.$message.success("删除成功")
          this.load()
        } else {
          this.$message.error("删除失败")
        }
        this.delFormVisible = false
      })
    },
    handleadd(){
      this.addFormVisible = true
    },
    handleEdit(row){
      this.timeForm =row
      this.addFormVisible = true
    },
    add(){
      this.$refs['timeForm'].validate((valid)=>{
        if (valid){
          request.post("/interview/save",this.timeForm).then(res =>{
            if(res){
              this.$message.success("保存成功")
              this.load()
              this.addFormVisible = false
            }else {
              this.$message.error("保存失败")
            }
          })
        }
      })
    },
    cancel(){
      this.addFormVisible = false
      this.form={}
      this.timeForm={}
    },
  }
}
</script>

<style scoped>

</style>