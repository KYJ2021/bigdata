<template>
  <div class="container">
    <!-- 顶部搜索栏 -->
    <div class="top-bar">
      <div class="logo">
        <img src="./assets/logo.png" alt="logo">
      </div>
      <div class="search-box">
        <input type="text" placeholder="搜索商家">
        <button>搜索</button>
      </div>
      <div class="user-profile">
        <img src="./assets/avatar.png" alt="avatar">
        <span>用户名</span>
      </div>
    </div>

    <!-- 推荐商户列表 -->
    <div class="recommendation">
      <h1>推荐商户</h1>
      <div class="list">
        <div v-for="item in list" :key="item.id" class="item">
          <div class="image">
            <img :src="item.image" alt="">
          </div>
          <div class="info">
            <h2>{{ item.title }}</h2>
            <p>{{ item.description }}</p>
            <div class="score">{{ item.score }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  data() {
    return {
      list: [
        {
          id: 1,
          title: "餐厅1",
          description: "这是餐厅1的描述",
          score: 4.5,
          image: "./assets/image1.jpg"
        },
        {
          id: 2,
          title: "餐厅2",
          description: "这是餐厅2的描述",
          score: 4.8,
          image: "./assets/image2.jpg"
        },
        {
          id: 3,
          title: "餐厅3",
          description: "这是餐厅3的描述",
          score: 4.6,
          image: "./assets/image3.jpg"
        }
      ]
    };
  }
};
</script>

<style scoped>
/* 全局样式 */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
}

/* 顶部搜索栏样式 */
.top-bar {
  background-color: #007bff;
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1;
}

.top-bar .logo img {
  height: 40px;
}

.top-bar .search-box input {
  padding: 10px;
  margin-right: 10px;
  width: 300px;
  border: none;
  border-radius: 5px;
}

.top-bar .search-box button {
  padding: 10px;
  background-color: #fff;
  color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.top-bar .user-profile img {
  height: 40px;
  margin-right: 10px;
}

/* 推荐商户样式 */
.recommendation {
  margin-top: 100px;
  padding: 20px;
}

.recommendation h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.recommendation .list {
  display: flex;
  flex-wrap: wrap;
}

.recommendation .item {
  margin-right: 20px;
  margin-bottom: 20px;
  width: calc(33.33% - 20px);
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid #ddd;
  border-radius: 5px;
 padding: 20px;
}

.recommendation .item .image {
  height: 200px;
  overflow: hidden;
  border-radius: 5px;
}

.recommendation .item .image img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}

.recommendation .item .info {
  margin-top: 10px;
  text-align: center;
}

.recommendation .item .info h2 {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.recommendation .item .info p {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.recommendation .item .info .score {
  font-size: 20px;
  font-weight: bold;
  color: #f90;
  margin-top: 10px;
}
</style>