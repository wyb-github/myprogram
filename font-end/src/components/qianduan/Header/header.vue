<template>
  <div class="head1">
    <div class="headbox">
      <div class="boxcenter">
        <span>在线时间 08:30 ~ 9:30</span>
        <span style="margin-left:40px">欢迎访问数码家电在线商城</span>
        <i class="shopcar el-icon-shopping-cart-1"></i>
        <div class="managebox">
          <span>欢迎，网站管理员！</span>
          <i></i>
        </div>
      </div>
    </div>
    <div class="headbox2">
      <div class="boxcenter box2">
        <div class="logo">
          <img src="../../../assets/headimg/logo.png" alt="logo">
        </div>
        <div class="menubox">
          <router-link to="/first">
            <div class="topmenu">首页</div>
          </router-link>
          <router-link to="/laptop">
            <div class="topmenu">笔记本</div>
          </router-link>
          <router-link to="/desktop">
            <div class="topmenu">台式机</div>
          </router-link>
          <router-link to="/peripheral">
            <div class="topmenu">外设系列</div>
          </router-link>
          <router-link to="/evalution">
            <div class="topmenu">评测中心</div>
          </router-link>
          <router-link to="/service">
            <div class="topmenu">售后服务</div>
          </router-link>
        </div>
        <div class="search">
          <div class="searchbox">
            <input type="text" placeholder="游戏笔记本">
            <i class="el-icon-search" style="color:#999;font-size:18px;"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
a{
    text-decoration: none;
}
.head1{
  width: 100%;
  height: 100%;
}
.headbox{
  width: 100%;
  height: 44px;
  background-color: #272727;
}
.headbox2{
  width: 100%;
  height: 98px;
  background-color: black;
  border-bottom: 2px solid #00EFF2;
}
.boxcenter{
  width: 1190px;
  /* height: 100%; */
  margin: 0 auto;
  color: #999;
  line-height: 44px;
  font-size: 12px;
  font-family: 微软雅黑, Helvetica, Arial, Verdana, sans-serif;
}
.managebox{
  float: right;
  color: #999;
  line-height: 44px;
  font-size: 12px;
  font-family: 微软雅黑, Helvetica, Arial, Verdana, sans-serif;
}
.shopcar{
  float:right;
  line-height: 44px;
  font-size: 18px;
  color:#999;
  margin-left: 10px;
}
.box2{
  display: flex;
  justify-content: space-between;
  height:75px;
  padding-top: 25px;
}
.mbxiala{
  background-color: #272727;
  color: #999;
  border-color:#272727; 
}
.logo{
  width: 237px;
  height:50px;
}
.logo img{
  width: 237px;
  height:50px;
}
.menubox{
  width: 676.8px;
  height: 47.6px;
  vertical-align: middle;
  float:left;
  display: flex;
  justify-content: space-between;
}
.topmenu{
  width: auto;
  height: 47.6px;
  color: #999;
  font-size: 14px;
}
.topmenu:hover{
  color:#00EFF2;
}
.search{
  width:200px;
  height: 76px;
  padding: 0 0 15px;
}
.searchbox{
  width: 100%;
  height: 37px;
  border:1px solid #999;
  line-height: 37px;
}
.searchbox input{
  height: 20px;
  margin-left: 10px;
  background-color: black;
  color: #999;
  border: none;
  outline: none;
}
</style>