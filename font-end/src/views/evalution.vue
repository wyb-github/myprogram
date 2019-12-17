<template>
    <div class="peripheral-page">
        <el-breadcrumb separator-class="el-icon-arrow-right" class="breadcrumb">
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>评测中心</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="gray-back">
            <div class="bigbox">
                <div class="sortbox">
                    <div class="sortitem"></div>
                    <div class="sortitem"></div>
                    <div class="sortitem"></div>
                    <div class="sortitem"></div>
                    <div class="sortitem"></div>
                </div>
                <div class="showbox">
                    <div class="commody" v-for="(item,index) in tableData" :key="index">
                        <!-- <img :src="{ require('../assets/laptapimg/'+item.img) }" alt=""> -->
                        <p class="text1">{{ item.name }}</p>
                        <p class="text2">￥5999</p>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
export default {
    data() {
      return {
        value: 0
      }
    },
    // mounted(){
    //     this.$axios.get("api/goods").then((response)=>{
    //         console.log(response.data)
    //         this.tableData = response.data.data
    //         console.log(response.data.data[0]['name'])
    //         console.log(response.data.data[0]['describe'])
    //     }).catch((error)=>{
    //         console.log(error)
    //     })
    // },
}
</script>

<style scoped>
.peripheral-page{
    width:100%;
    height: auto;
}
.breadcrumb{
    width: 1190px;
    margin: 20px auto;
    background-color: white;
}
.gray-back{
    width: 100%;
    height: 500px;
    background-color: #f2f2f2;
    border-top: 1px solid #f2f2f2;
}
.bigbox{
    width: 1190px;
    height: auto;
    margin: 20px auto;
}
.sortbox{
    width: 218px;
    height: 264px;
    background-color: white;
    padding: 20px 20px;
    display: inline-block;
}
.showbox{
    width: 960px;
    height: 400px;
    background-color: antiquewhite;
    float: right;
    display: flex;
    justify-content:space-between;
}
.commody{
    width: 304px;
    height: 333px;
    background-color: white;
}
.commody img{
    width:100%;
    height: 209px;
}
.text1{
    color: #191919;
    font-size: 15px;
    font-family: 微软雅黑;
    text-align: center;
}
.text2{
    color: #dd3333;
    font-size: 18px;
    font-family: 微软雅黑;
    text-align: center;
}
</style>