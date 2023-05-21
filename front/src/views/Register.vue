<template>
  <div style="margin: 100px auto; background-color: #fff; width: 450px; height: 400px; padding: 20px; border-radius: 20px; box-shadow: 5px 8px 20px rgba(40,41,47,0.35);">
    <div style="margin: 20px 0; text-align: center; font-size: 24px"><b>注 册</b></div>
    <el-form ref="userForm" :model="form" :rules="rules" label-width="40px">
      <el-form-item style="margin-top: 50px" prop="username">
        <el-input v-model="form.username" style="width: 340px" prefix-icon="el-icon-user"></el-input>
      </el-form-item>
      <el-form-item style="margin-top: 30px" prop="password">
        <el-input v-model="form.password" style="width: 340px" prefix-icon="el-icon-lock"></el-input>
      </el-form-item>
      <el-form-item style="margin-top: 50px">
        <el-button style="width: 340px" type="primary" @click="Submit">提交</el-button>
      </el-form-item>
      <el-form-item>
        <router-link to="/login">
          <el-button style="width: 340px">返回</el-button>
        </router-link>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Register",
  data() {
    return {
      form: {
        userType: 2,
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
        ],
      }
    }
  },
  methods: {
    Submit() {
      this.$refs['userForm'].validate((valid) => {
        if (valid) {  // 表单校验合法
          request.post("/user", this.form).then(res => {
            if (res.code==='200') {
              this.$message.success("提交成功")
              this.$router.push("/login")
            } else {
              this.$message.error(res.msg)
            }
          })
        }
      });
    }
  }
}
</script>

<style scoped>

</style>