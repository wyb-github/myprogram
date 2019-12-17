<template>
    <div class="index">
        <el-container>
            <el-header>
                <Head></Head>
            </el-header>
            <el-main>
                <router-view></router-view>
            </el-main>
            <el-footer>
                <Foot></Foot>
            </el-footer>
        </el-container>
    </div>
</template>
<script>
import Head from "@/components/qianduan/Header/header.vue";
import Foot from "@/components/qianduan/Footer/footer.vue";

export default {
    name: 'index',
    components: {
        Head,
        Foot,
    }
}
</script>
<style scoped>
*{
    margin: 0;
    padding: 0;
    list-style: none;
}
a{
    text-decoration: none;
}
.index{
    width: 100%;
    height: 100%;
}
.el-header{
    width: 100%;
    height: 142px!important;
    padding: 0;
    background-color: red;
  }
.el-container{
    width: 100%;
    height: 100%;
}

</style>