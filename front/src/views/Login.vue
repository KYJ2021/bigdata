<template>
  <div class="wrapper">
    <div style="margin: 100px 900px; background-color: #fff; width: 350px; height: 400px; padding: 20px; border-radius: 20px; box-shadow: 5px 8px 20px rgba(40,41,47,0.35);">
      <div style="margin: 40px 0; text-align: center; font-size: 20px"><b>登录点评推荐系统</b></div>
      <el-form :model="user" :rules="rules" ref="userForm">
        <el-form-item prop="username">
          <el-input size="medium" style="margin: 10px 0" prefix-icon="el-icon-user" v-model="user.username"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input size="medium" style="margin: 10px 0" prefix-icon="el-icon-lock" show-password v-model="user.password1"></el-input>
        </el-form-item>
        <el-form-item style="margin: 35px; text-align: center">
          <el-button type="primary" size="small"  style="margin-right: 50px" autocomplete="off" @click="login">登录</el-button>
          <router-link to="/register">
            <el-button type="warning" size="small"  autocomplete="off">注册</el-button>
          </router-link>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      user: {'password': '666'},
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
    login() {
      this.$refs['userForm'].validate((valid) => {
        if (valid) {  // 表单校验合法
          this.request.get("/login",{
            params: {
              username: this.user.username,
            }
          }).then(res => {
            if(res){
              localStorage.setItem("user", JSON.stringify(res.data[0]))  // 存储用户信息到浏览器
              this.user=JSON.parse(localStorage.getItem("user"))
              if(this.user.userType==1){
                this.$router.push("/user")
              }else {
                this.$router.push("/")
              }
              this.$message.success("登录成功")
            }else {
              this.$message.error("登录失败")
            }
          })
        }
      });
    }
    // login() {
    //   localStorage.setItem("user", '{"id":1,"username":"test","userType":1}')  // 存储用户信息到浏览器（这里先随便写一个，因为还没写后端，写这行代码是因为系统要判定浏览器中是否有缓存的用户信息，否则路由保护）
    //   this.$router.push("/")
    //   this.$message.success("登录成功")
    // }
  }
}
</script>

<style scoped>
.wrapper{
  height: 100vh;
  background-image: url("../assets/undraw_online_test_re_kyfx (1).svg");
  background-size: 540px 300px;
  background-position: 250px 200px;
  background-repeat: no-repeat;
  overflow: hidden;
}

</style>
