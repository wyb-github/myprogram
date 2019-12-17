<template>
    <div class="laptop-page">
        <el-breadcrumb separator-class="el-icon-arrow-right" class="breadcrumb">
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>笔记本</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="gray-back">
            <div class="bigbox">
                <div class="sortbox">
                    <div class="sortitem">
                        <div>品牌</div>
                        <select class="form-control c1">
                            <option>---请选择---</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>
                    </div>
                    <div class="sortitem">
                        <div>处理器</div>
                        <select class="form-control c1">
                            <option>---请选择---</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>
                    </div>
                    <div class="sortitem">
                        <div>显卡</div>
                        <select class="form-control c1">
                            <option>---请选择---</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>
                    </div>
                    <div class="sortitem">
                        <div>屏幕尺寸</div>
                        <select class="form-control c1">
                            <option>---请选择---</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>
                    </div>
                    <div class="sortitem">
                        <div>内存</div>
                        <select class="form-control c1">
                            <option>---请选择---</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>
                    </div>
                    <div class="sortitem">
                        <div>硬盘</div>
                        <select class="form-control c1">
                            <option>---请选择---</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>
                    </div>
                    <div class="sortitem">
                        <div>价格</div>
                        <input type="range" name="slider-1" id="slider-1" min="1" max="15000" step="1" v-model="value">
                        <div style="font-size:12px;color:#333;margin-top:5px;">
                            <span>价格：</span>
                            <span>￥{{ value }}</span>
                        </div>
                    </div>
                </div>
                <div class="showbox">
                    <div class="commody" v-for="(item,index) in tableData" :key="index">
                        <img src="../assets/laptapimg/ass1.jpg" alt="">
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
    mounted(){
        this.$axios.get("api/goods").then((response)=>{
            window.console.log(response.data.msg)
            this.tableData = response.data.msg
            window.console.log(response.data.msg[0]['name'])
            window.console.log(response.data[0]['describe'])
        }).catch((error)=>{
            window.console.log(error)
        })
    },
}
</script>

<style scoped>
.laptop-page{
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
    height: 100%;
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
    height: 544px;
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
.sortitem{
    margin: 10px 0;
}
.sortitem div{
    color: #333;
    font-size: 16px;
    margin-bottom: 8px;
    font-family: 微软雅黑;
}
.c1{
    height: 30px;
    font-size: 13px;
    border-radius: 0px;
    line-height: 30px;
    font-family: 微软雅黑;
    box-shadow: 0 0 0 0;
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