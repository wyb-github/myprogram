<template>
    <div class="foot">
        <div class="footbox1">
            <div class="servicebox">
                <div class="service">
                    <img src="../../../assets/footimg/small1.png" alt="">
                    <div>三年免费保修</div>
                </div>
                <div class="service">
                    <img src="../../../assets/footimg/small2.png" alt="">
                    <div>七天无理由退货</div>
                </div>
                <div class="service">
                    <img src="../../../assets/footimg/small3.png" alt="">
                    <div>15天免费换货</div>
                </div>
                <div class="service">
                    <img src="../../../assets/footimg/small4.png" alt="">
                    <div>满150元包邮</div>
                </div>
                <div class="service">
                    <img src="../../../assets/footimg/small5.png" alt="">
                    <div>200余家售后网点</div>
                </div>
            </div>
            <div class="jieshaobox">
                <div class="jieshao">
                    <div>
                        <li>帮助中心</li>
                        <li>购物指南</li>
                        <li>支付方式</li>
                        <li>配送方式</li>
                    </div>
                    <div>
                        <li>服务支持</li>
                        <li>报修政策</li>
                        <li>服务标准</li>
                        <li>退换货政策</li>
                    </div>
                    <div>
                        <li>关于我们</li>
                        <li>公司介绍</li>
                        <li>加入我们</li>
                        <li>联系我们</li>
                    </div>
                    <div>
                        <li>新闻资讯</li>
                        <li>营业执照</li>
                        <li>新闻动态</li>
                        <li>版权声明</li>
                    </div>
                    <div>
                        <li>线下门店</li>
                        <li>法律声明</li>
                        <li>隐私政策</li>
                        <li>服务条款</li>
                    </div>
                </div>
                <div class="erweimabox">
                    <p>微信公众化</p>
                    <img src="../../../assets/footimg/guanzhu.jpg" alt="">
                </div>
                <div class="callmebox">
                    <div>4006-999-999</div>
                    <div>周一至周日 8:00-18:00</div>
                    <div>24小时在线客服</div>
                </div>
            </div>
        </div>
        <div class="footbox2">
              版权所有2056-2086 数码家电在线商城模板  沪ICP 备000000000号-0
        </div>
    </div>
</template>

<script>
export default {
    name:'foot',
}
</script>

<style scoped>
.foot{
    width:100%;
    height: 322px;
}
.footbox1{
    width:100%;
    height:280px;
    background-color: #272727;
}
.footbox2{
    width:100%;
    height:41px;
    background-color: #000;
    color:#999;
    font-size: 12px;
    text-align: center;
    line-height: 41px;
}
.servicebox{
    width: 1190px;
    height: 76px;
    margin:0 auto;
    border-bottom: 2px solid #373737;
    display: flex;
    justify-content: space-between;
}
.service{
    width: 180px;
    height: 100%;
    line-height: 76px;
    color: #999;
    font-size: 16px;
    font-family: 微软雅黑, Helvetica, Arial, Verdana, sans-serif;
    display: flex;
}
.service img{
    width: 24px;
    height:24px;
    margin-top:24px;
}
.service div{
    padding-left: 10px;
}
.jieshaobox{
    width: 1190px;
    margin: 0 auto;
    height: auto;
    display: flex;
    justify-content: space-between;
}
.jieshao{
    width: 750px;
    height: 108px;
    margin-top:40px;
    display: flex;
    justify-content: space-between;
    color: #999;
    font-size: 12px;
}
.jieshao div{
    line-height: 27px;
}
.jieshao div li:first-child{
    font-size: 16px;
}
.erweimabox{
    width: 100px;
    height: auto;
    margin-top: 40px;
    line-height: 30px;
}
.erweimabox p{
    color:#999;
    font-size: 16px;
}
.erweimabox img{
    width: 79px;
    height: 79px;
}
.callmebox{
    width: 170px;
    height: auto;
    margin-top:40px;
    line-height: 35px;
}
.callmebox div:first-child{
    width: 162px;
    text-align: center;
    font-size: 26px;
    color:#00eff2;
}
.callmebox div:nth-child(2){
    width: 162px;
    height: 40px;
    text-align: center;
    font-size: 12px;
    color: #999;
}
.callmebox div:last-child{
    width: 135px;
    height: 28px;
    margin:0 auto;
    text-align: center;
    line-height: 20px;
    border:1px solid #00eff2;
    padding: 4px 0px;
    color: #00eff2;
    font-size: 14px;
}
</style>