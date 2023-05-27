<template>
    <div class="main-page">
        <header class="header">
            <div class="logo" style="margin-top: 25px">
                <i class="el-icon-location" style="margin-right: 5px; color: #0073ff"></i>
                <el-link type="info">{{city}}</el-link>
            </div>
            <div class="search">
                <input placeholder="搜索商家、品类或商圈" v-model="searchValue" class="search-input" style="width: 500px"></input>
                <el-button type="primary" icon="el-icon-search" @click="handleSearch" style ="margin-left: 5px" round>搜索</el-button>
            </div>
            <div>
                <el-link type="info">hello {{user.nickname}}!</el-link>
                <el-link type="danger" style="margin-left: 10px" @click="logout">退出</el-link>
            </div>
        </header>
        <el-main class="content">
            <template>
              <el-carousel :interval="4000" type="card" height="400px">
                <el-carousel-item v-for="item in 6" :key="item">
                  <h3 text="2xl" justify="center">{{ item }}</h3>
                </el-carousel-item>
              </el-carousel>
            </template>
            <div class="recommend" style="margin-left: 50px">
                <h2 style="color: #666666">为你推荐</h2>
                <el-row :gutter="24" class="cards">
                    <el-col :span="5" v-for="(card, index) in recommendCards" :key="index">
                        <el-card :body-style="{ padding: '0px' }" shadow="hover" @click.native="handleCardClick(card)">
                            <div style="padding: 14px;">
                                <span class="card-title">{{ card.title }}</span>
                                <div class="card-price">{{ card.price }}</div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </div>
            <div class="friends" style="margin-left: 50px">
                <h2 style="color: #666666">可能认识的人</h2>
                <el-row :gutter="24" class="cards">
                    <el-col :span="4" v-for="(card, index) in friends" :key="index">
                        <el-card :body-style="{ padding: '0px' }" shadow="hover" @click.native="handleCardClick(card)">
                            <div style="padding: 14px;">
                                <span class="card-title" style="font-size: 23px; color: #393939">{{ card.friend_name }}</span>
                                <div style="color: #dcc85d;margin-left: 10px">
                                    <img src="../assets/white-medium-star.svg" style="width: 23px; position: relative; top: 5px; right: 5px">
                                    {{ card.fans }}
                                </div>
                                <div style="margin-left: 10px;color: #f09389">
                                    <img src="../assets/red-heart.svg" style="width: 20px; position: relative; top: 5px; right: 5px">
                                    {{ card.rewards }}
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </div>
        </el-main>
        <el-footer class="footer">
            <div class="links">
                <span>关于我们</span>
                <span>联系我们</span>
                <span>加入我们</span>
                <span>用户协议</span>
                <span>隐私政策</span>
            </div>
            <div class="copy"> © 2023 某某科技有限公司 版权所有 </div>
        </el-footer>
    </div>
</template>
<script>
    import request from "@/utils/request";
export default {
data() {
    return {
        user: JSON.parse(localStorage.getItem("user")),
        city: 'new york',
        searchValue: '',
        recommendCards: [
            { title: '汉堡王',
                price: '¥ 20',
                image: '../assets/card1.jpg',
            },
            { title: '必胜客',
                price: '¥ 50',
                image: '../assets/card2.jpg',
            },
            { title: '星巴克',
                price: '¥ 30',
                image: '../assets/card3.jpg',
            },
            { title: '肯德基',
                price: '¥ 25',
                image: '../assets/card4.jpg',
            },
            { title: '麦当劳',
                price: '¥ 22',
                image: '../assets/card5.jpg',
            },
            { title: '必胜客',
                price: '¥ 50',
                image: '../assets/card6.jpg',
            },
            { title: '星巴克',
                price: '¥ 30',
                image: '../assets/card7.jpg',
            },
            { title: '肯德基',
                price: '¥ 25',
                image: '../assets/card8.jpg',
            },
        ],
        friends: [],
    };
    },
    created(){
        this.load()
    },
methods: {
    load(){
        request.get("/user/friend",{
            params: {
                user: this.user.id
            }
        }).then(res => {
            this.friends=res
            console.log(this.friends)
        })
    },
    handleMenuSelect(index) {
        console.log(`选择了菜单${index}`);
        },
    handleSearch() {
        console.log(`搜索了${this.searchValue}`);
        },
    handleCardClick(card) {
        console.log(`点击了${card.title}`);
        },
    logout() {
      this.$router.push("/login")
      localStorage.removeItem("user")
      this.$message.success("退出成功")
    },
},
};
</script>
<style scoped>
    .main-page {
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .header {
      height: 60px;
      background-color: #fff;
      box-shadow: 0 20px 4px rgba(0, 0, 0, 0.1);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
    }
    .flex-grow {
      flex-grow: 1;
    }
    .logo {
        width: 100px;
        height: 50px;
    }
    img {
        width: 100%;
        height: 100%;
    }
    .nav {
      display: flex;
      list-style: none;
      margin: 0;
      padding: 0;
    }
    .el-menu-item {
        padding: 0 20px;
    }
    :hover {
        background-color: transparent;
    }
    :active {
        background-color: transparent;
    }
    .search {
        display: flex;
        align-items: center;
    }
    .search input {
      border: none;
      border-radius: 20px;
      padding: 8px 16px;
      font-size: 16px;
      outline: none;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .content {
        flex: 1;
        padding: 30px;
        background-color: #f5f5f5;
        overflow-y: auto;
    }
    .banner {
        height: 400px;
    }
    .el-carousel__item h3 {
      color: #475669;
      opacity: 0.75;
      line-height: 200px;
      margin: 0;
      text-align: center;
    }

    .el-carousel__item:nth-child(2n) {
      background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n + 1) {
      background-color: #d3dce6;
    }
    img {
        width: 100%;
        height: 100%;
    }
    .recommend {
        margin-top: 30px;
    }
    h2 {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .cards {
        margin: 0 -12px;
    }
    .el-col {
        margin: 12px;
    }
    .card-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    .card-title {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 10px;
        display: block;
    }
    .card-price {
        font-size: 18px;
        font-weight: bold;
        color: #ff4949;
        margin-bottom: 10px;
    }
    .hot-deals {
        margin-top: 30px;
    }
    h2 {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .deals {
        margin: 0 -12px;
    }
    .el-col {
        margin: 12px;
    }
    .card-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    .card-title {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 10px;
        display: block;
    }
    .card-price {
        font-size: 18px;
        font-weight: bold;
        color: #ff4949;
        margin-bottom: 10px;
    }
    .card-label {
        font-size: 14px;
        margin-top: 10px;
        color: #999;
    }
    .footer {
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 30px;
        background-color: #f5f5f5;
        font-size: 14px;
    }
    .links {
        display: flex;
        align-items: center;
    }
    span {
        margin-right: 20px;
        cursor: pointer;
    }
</style>