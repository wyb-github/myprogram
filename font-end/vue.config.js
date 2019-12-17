// vue.config.js
module.exports = {
  // 选项...
  devServer:{
    open: true,   // 启动项目后自动开启浏览器
    host:'127.0.0.1',
    port:'8000',  // 端口号
    proxy: {
      "/api": {
        target: "http://127.0.0.1:5000/",
        changeOrigin: true,  // 是否代理呢
      }
    }
  }
}