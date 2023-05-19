<template>
  <div class="main-page">
    <header class="header">
      <div class="logo">
        <img src="../assets/logo.png" alt="logo" />
      </div>
      <nav class="nav">
        <ul>
          <li><a href="#">首页</a></li>
          <li><a href="#">美食</a></li>
          <li><a href="#">电影</a></li>
          <li><a href="#">酒店</a></li>
          <li><a href="#">KTV</a></li>
          <li><a href="#">优惠</a></li>
        </ul>
      </nav>
      <div class="search">
        <input type="text" placeholder="搜索商家、品类或商圈" />
        <button>搜索</button>
      </div>
    </header>
    <div class="content">
      <div class="banner">
        <img src="../assets/banner.jpg" alt="banner" />
      </div>
      <div class="recommend">
        <h2>为你推荐</h2>
        <div class="cards">
          <div class="card">
            <img src="../assets/card1.jpg" alt="card1" />
            <h3>麦当劳</h3>
            <p>快餐, ￥20/人</p>
          </div>
          <div class="card">
            <img src="../assets/card2.jpg" alt="card2" />
            <h3>星巴克</h3>
              <p>咖啡, ￥30/人</p>
          </div>
          <div class="card">
            <img src="../assets/card3.jpg" alt="card3" />
            <h3>肯德基</h3>
            <p>快餐, ￥15/人</p>
          </div>
          <div class="card">
            <img src="../assets/card4.jpg" alt="card4" />
            <h3>必胜客</h3>
            <p>披萨, ￥50/人</p>
          </div>
        </div>
      </div>
      <div class="hot-deals">
        <h2>热门优惠</h2>
        <div class="deals">
          <div class="deal">
            <img src="../assets/deal1.jpg" alt="deal1" />
            <div class="info">
              <h3>麦当劳优惠券</h3>
              <p>仅限堂食, 9折优惠</p>
            </div>
          </div>
          <div class="deal">
            <img src="../assets/deal2.jpg" alt="deal2" />
            <div class="info">
              <h3>必胜客披萨套餐</h3>
              <p>2人份, ￥69</p>
            </div>
          </div>
          <div class="deal">
            <img src="../assets/deal3.jpg" alt="deal3" />
            <div class="info">
              <h3>星巴克会员专享</h3>
              <p>买一送一, 限时优惠</p>
            </div>
          </div>
          <div class="deal">
            <img src="../assets/deal4.jpg" alt="deal4" />
            <div class="info">
              <h3>肯德基超值套餐</h3>
              <p>3人份, ￥59</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer class="footer">
      <div class="links">
        <ul>
          <li><a href="#">关于我们</a></li>
          <li><a href="#">联系我们</a></li>
          <li><a href="#">加入我们</a></li>
          <li><a href="#">服务条款</a></li>
        </ul>
      </div>
      <div class="social-media">
        <ul>
          <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
          <li><a href="#"><i class="fab fa-twitter"></i></a></li>
          <li><a href="#"><i class="fab fa-instagram"></i></a></li>
          <li><a href="#"><i class="fab fa-linkedin-in"></i></a></li>
        </ul>
      </div>
      <div class="newsletter">
        <h3>订阅电子邮件通讯</h3>
        <form>
          <input type="email" placeholder="输入你的电子邮件地址" />
          <button>订阅</button>
        </form>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "MainPage",
};
</script>

<style>
.main-page {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

/*header*/
.header {
  height: 80px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
}

.logo img {
  height: 40px;
}

.nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav li {
  margin-right: 16px;
}

.nav a {
  color: #666;
  font-size: 16px;
  text-decoration: none;
}

.nav a:hover {
  color: #f60;
}

.search input {
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  font-size: 16px;
  outline: none;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.search button {
  background-color: #f60;
  color: #fff;
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  font-size: 16px;
  outline: none;
  cursor: pointer;
 }

.search button:hover {
  background-color: #ff872c;
}
/*content*/
.content {
  flex: 1;
  display:flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.banner img {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.recommend {
  margin-top: 32px;
}

.recommend h2 {
  font-size: 24px;
  margin-bottom: 16px;
}

.cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.card {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  text-align: center;
  transition: all 0.3s ease-in-out;
}

.card:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  transform: translateY(-4px);
}

.card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card h3 {
  font-size: 18px;
  margin-top: 16px;
}

.card p {
  color: #999;
  font-size: 14px;
  margin-top: 8px;
}

.hot-deals {
  margin-top: 48px;
}

.hot-deals h2 {
  font-size: 24px;
  margin-bottom: 16px;
}

.deals {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.deal {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: all 0.3s ease-in-out;
}

.deal:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  transform: translateY(-4px);
}

.deal img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.deal .info {
  padding: 16px;
}

.deal h3 {
  font-size: 18px;
  margin-bottom: 8px;
}

.deal p {
  color: #999;
  font-size: 14px;
  margin-top: 8px;
}
/*footer*/
.footer {
  background-color: #f8f8f8;
  padding: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.links ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.links li {
  margin-right: 16px;
}

.links a {
  color: #666;
  font-size: 14px;
  text-decoration: none;
}

.links a:hover {
  color: #f60;
}

.social-media ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.social-media li {
  margin-right: 16px;
}

.social-media a {
  color: #666;
  font-size: 24px;
  text-decoration: none;
}

.social-media a:hover {
  color: #f60;
}

.newsletter h3 {
  font-size: 18px;
  margin-bottom: 16px;
}

.newsletter form {
  display: flex;
}

.newsletter input {
  flex: 1;
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  font-size: 14px;
  outline: none;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.newsletter button {
  background-color: #f60;
  color: #fff;
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  font-size: 14px;
  outline: none;
  cursor: pointer;
}

.newsletter button:hover {
  background-color: #ff872c;
}
    /*渐变动画 */
.header {
  background: linear-gradient(to bottom, #fff, rgba(255, 255, 255, 0));
  animation: header-fade 1s ease-in-out forwards;
}

@keyframes header-fade {
  from {
    background: linear-gradient(to bottom, #fff, rgba(255, 255, 255, 0));
  }
  to {
    background: #fff;
  }
}

/* 然后，我们为内容区域添加一个缩放动画 */
.content {
  animation: content-zoom 1s ease-in-out forwards;
}

@keyframes content-zoom {
  from {
    transform: scale(0.5);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

/* 最后，我们为底部添加一个弹跳动画 */
.footer {
  animation: footer-bounce 1s ease-in-out forwards;
}

@keyframes footer-bounce {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0);
  }
}
</style>